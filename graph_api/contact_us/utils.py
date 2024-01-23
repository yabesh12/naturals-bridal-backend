import os

from apps.contact_us.models import ContactEnquiry
from naturals_bridal_be.settings import get_list
from django.core.mail import send_mail
import threading


def send_email_to_customer(contactEnquiryObject: ContactEnquiry):
    """
    Send Email to Customer
    """
    recipient_list = [
        contactEnquiryObject.email,
    ]
    subject = f"{contactEnquiryObject.first_name.capitalize()}, Confirmation of Your Bridal Makeup Request "
    message = f"""Hey there, {contactEnquiryObject.first_name.capitalize()}! 

Thanks a bunch for reaching out to us! Our experts are already gearing up to assist you and will be in touch super soon!

While we work our magic behind the scenes, why not take a delightful stroll through our site? Explore the makeup trends, inspiring bridal looks, makeup secrets, and unveil an inspiration for your dream bridal look.

Your interest means the world to us, and we can't wait to make you feel fabulous! ✨

Stay tuned for the best beauty experience ever!

Warmest wishes,
Naturals Bridal Team"""

    threading.Thread(
        target=custom_send_email, args=(subject, message, recipient_list)
    ).start()
    return True


def send_email_to_admin(contactEnquiryObject: ContactEnquiry, subject=None):
    """
    Send Email to Admin
    """
    recipient_list = get_list(os.environ.get("ADMIN_EMAIL_LIST", "yabesh@deepsense.in"))
    subject_text = "New Bridal Request Received"
    empty = "NA"

    service = subject.get("Service", "")
    artist = subject.get("Artist", "")
    enquiry_type = subject.get("Subject", "")

    subject_lines = []
    if enquiry_type and enquiry_type != 'OTHERS':
        subject_type = enquiry_type
    else:
        subject_type = "OTHERS"
        if service:
            subject_lines.append(f"Service: {service}")
        if artist:
            subject_lines.append(f"Artist: {artist}")

    subject_line = "\n".join(subject_lines)

    message = f"""Dear Team,

We wanted to inform you that a new appointment has been booked with Naturals Bridal. Kindly reach out to the customer as soon as possible to understand their query and provide any necessary information.

Customer Details:
Name: {contactEnquiryObject.first_name.capitalize()} {contactEnquiryObject.last_name.capitalize()}
Phone: {contactEnquiryObject.phone_number}
Email: {contactEnquiryObject.email}
Subject: {subject_type}
{subject_line}

Please ensure to contact the customer promptly to offer a warm confirmation and address any questions they may have. It is important to provide exceptional customer service and make them feel valued throughout their bridal journey.

Best Regards,
Naturals Bridal Management"""
    threading.Thread(
        target=custom_send_email, args=(subject_text, message, recipient_list)
    ).start()
    return True


def custom_send_email(subject, message, recipient_list):
    """
    Send Email
    """
    from_email = os.environ.get("FROM_EMAIL", "test@test.com")
    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except Exception as e:
        print(e)
