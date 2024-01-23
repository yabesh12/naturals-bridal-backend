import graphene
from graphene_django import DjangoObjectType

from apps.contact_us.models import ContactEnquiry, Address


class ContactEnquiryType(DjangoObjectType):
    """
    Graphene DjangoObjectType for ContactEnquiry Model
    """

    class Meta:
        model = ContactEnquiry
        exclude = ("created_at", "updated_at")
        interfaces = (graphene.relay.Node,)


class AddressType(DjangoObjectType):
    """
    Graphene DjangoObjectType for Address Model
    """

    class Meta:
        model = Address
        exclude = ("created_at", "updated_at")
        interfaces = (graphene.relay.Node,)
