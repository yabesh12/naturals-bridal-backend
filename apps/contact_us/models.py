from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models

from apps.carousel.models import Carousel
from apps.core.models import TimestampModel
from apps.service.models import Service

ENQUIRY_TYPE_CHOICES = (
    ("GENERAL_ENQUIRY", "GENERAL ENQUIRY"),
    ("OVERALL_PACKAGE", "OVERALL PACKAGE"),
    ("BRAND_PARTNERS", "BRAND PARTNERS"),
    ("OTHERS", "OTHERS"),
)


class Address(TimestampModel):
    """
    A model representing an address
    """
    address_line1 = models.CharField(max_length=200, blank=True, null=True)
    address_line2 = models.CharField(max_length=200, blank=True, null=True)
    landmark = models.CharField(max_length=100, null=True, blank=True, help_text="The nearby landmark")
    city = models.CharField(max_length=50, blank=True, null=True, help_text="City Name")
    state = models.CharField(max_length=50, blank=True, null=True, help_text="State Name")
    country = models.CharField(max_length=50, blank=True, null=True, help_text="Country Name")
    pincode = models.PositiveIntegerField(blank=True, null=True, help_text="Address Pincode")
    mobile = ArrayField(models.CharField(max_length=256, blank=True, null=True), default=list, blank=True, null=True,
                        help_text="Mobile number")
    email = ArrayField(models.CharField(max_length=256), default=list, help_text="Email Address")
    is_active = models.BooleanField(default=True, help_text="Status")
    is_default = models.BooleanField(default=False, help_text="Used For Default Address")
    full_address = models.TextField(max_length=1000, blank=True, null=True, help_text="Represents Full Address")

    class Meta:
        verbose_name_plural = 'Address'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} - {self.city} - {self.state} - {self.pincode}"

    def clean(self):
        if self.full_address and self.address_line1:
            raise ValidationError("Please either provide full address or single address lines")
        return None


class ContactEnquiry(TimestampModel):
    """
    To save the Contact us enquiries Django model
    """
    first_name = models.CharField(max_length=40, help_text="Enquiry person's first name")
    last_name = models.CharField(max_length=40, help_text="Enquiry person's last name")
    email = models.EmailField(max_length=255, help_text="Enquiry person's email")
    phone_number = models.CharField(max_length=10, help_text="Enquiry person's mobile number")
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True,
                                help_text="The service enquiring about")
    artist = models.ForeignKey(Carousel, on_delete=models.SET_NULL, blank=True, null=True,
                               help_text="The service enquiring about")
    message = models.TextField(max_length=1000, blank=True, null=True, help_text="The Enquiry Message")
    enquiry_type = models.CharField(max_length=50, choices=ENQUIRY_TYPE_CHOICES, help_text="The Enquiry Type")

    class Meta:
        verbose_name_plural = 'Enquiries (Contact Us)'

    def __str__(self):
        return self.first_name
