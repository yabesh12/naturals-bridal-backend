from graph_api.contact_us.utils import send_email_to_admin, send_email_to_customer
import graphene
from django.core.validators import validate_email
from graphql import GraphQLError
from graphql_relay import from_global_id
from apps.carousel.models import Carousel
from apps.contact_us.models import ContactEnquiry
from apps.core.utils import validate_mobile_number
from apps.service.models import Service
from graph_api.contact_us.enum import EnquiryTypeEnum
from graph_api.contact_us.types import ContactEnquiryType


class ContactEnquiryMutation(graphene.Mutation):
    """
    Used to Booking the Appointment

    Parameters
    ----------

    first_name : str
        the enquiry person's first name

    last_name: str
        the enquiry person's last name

    email: str
        the enquiry person's Email ID

    mobile_number : str
        the enquiry person's Mobile number

    service_ID : graphene ID (optional)
        The specific Service ID during the Enquiry

    artist_ID : graphene ID (optional)
        The specific Artist ID during the Enquiry

    Enquiry Type : Enum
        Form Type while submit the Contact Us Form

    message : str  (optional)
        Enquiry Message

    Returns
    -------
    contact_detail : ContactEnquiry ObjectType
        Json response of the current Contact Enquiry Details

    status : str
        Success text

    message : str
        response text

    Raises
    ------
    GraphQLError
        If mobile or email is Invalid
        or
        If service is not found
    """

    class Arguments:
        first_name = graphene.String(required=True, description="The Enquiry person's First Name")
        last_name = graphene.String(required=True, description="The Enquiry person's Last Name")
        email = graphene.String(required=True, description="The Enquiry person's Email ID")
        mobile_number = graphene.String(required=True, description="The Enquiry person's mobile number")
        service_id = graphene.ID(description="The service graphene ID is utilized during the Contact Us Form")
        artist_id = graphene.ID(description="The specific artist graphene ID during the Contact Enquiry")
        enquiry_type = EnquiryTypeEnum(required=True, description="The Enquiry Type Enum Field")
        message = graphene.String(description="The message provided in the enquiry")

    contact_detail = graphene.Field(ContactEnquiryType, description="ContactEnquiry DjangoObjectType")
    status = graphene.String(description="Status of the Endpoint")
    message = graphene.String(description="The return message")

    def mutate(self, info, first_name, last_name, email, mobile_number, enquiry_type, **kwargs):
        # get service id, artist id from kwargs
        service_id = kwargs.get("service_id")
        artist_id = kwargs.get("artist_id")
        subject_dict = {}

        # empty dict used to create the whole object
        data_dict = {}

        # validation for Enquiry Subject, it should be one subject during form submission
        if service_id and artist_id:
            raise GraphQLError("please provide either Service ID or Artist ID")

        # validate mobile and validate email
        validate_mobile_number(mobile_number)
        validate_email(email)

        # validation for firstname, lastname and message
        if len(first_name) < 2 or not first_name.isalpha():
            raise GraphQLError("please provide a valid first name")
        if len(last_name) < 2 or not last_name.isalpha():
            raise GraphQLError("please provide a valid last name")
        enquiry_msg = kwargs.get("message", "").strip()
        if not enquiry_msg or len(enquiry_msg) < 2:
            raise GraphQLError("Please provide a valid message")

        # get the service object
        if service_id:
            try:
                service_obj = Service.objects.get(id=from_global_id(service_id)[1])
                data_dict.update(
                    {"first_name": first_name, "last_name": last_name, "phone_number": mobile_number, "email": email,
                     "enquiry_type": EnquiryTypeEnum.OTHERS.value, "message": enquiry_msg, "service": service_obj})
                subject_dict.update({"Service":service_obj.title})
            except Service.DoesNotExist:
                raise GraphQLError("Service Does not Exist!")
            except ValueError:
                raise GraphQLError("Service ID is not valid")

        # get the artist object
        if artist_id:
            try:
                artist_obj = Carousel.objects.get(id=from_global_id(artist_id)[1])
                data_dict.update(
                    {"first_name": first_name, "last_name": last_name, "phone_number": mobile_number, "email": email,
                     "enquiry_type": EnquiryTypeEnum.OTHERS.value, "message": enquiry_msg, "artist": artist_obj})
                subject_dict.update({"Artist":artist_obj.title})
            except Carousel.DoesNotExist:
                raise GraphQLError("Artist Does not Exist!")
            except ValueError:
                raise GraphQLError("Artist ID is not valid")

        # for other general enquiries
        if not service_id and not artist_id:
            if enquiry_type.name == "OTHERS":
                raise GraphQLError("Please provide a valid Enquiry Type as no service or artist has been provided")
            data_dict.update(
                {"first_name": first_name, "last_name": last_name, "phone_number": mobile_number, "email": email,
                 "enquiry_type": enquiry_type.name, "message": enquiry_msg})
            subject_dict.update({"Subject": enquiry_type.name})
        try:
            contact_enquiry_obj = ContactEnquiry.objects.create(**data_dict)
            send_email_to_customer(contact_enquiry_obj)
            send_email_to_admin(contact_enquiry_obj, subject=subject_dict)
        except Exception as e:
            raise GraphQLError(e)

        return ContactEnquiryMutation(contact_detail=contact_enquiry_obj, status="SUCCESS",
                                      message="Contact Form Submitted Successfully!")


class ContactUsMutation(graphene.ObjectType):
    contact_enquiry = ContactEnquiryMutation.Field()
