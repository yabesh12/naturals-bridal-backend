from django.db import models
from versatileimagefield.fields import VersatileImageField

from apps.core.models import TimestampModel

GENDER_CHOICES = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
)


class Service(TimestampModel):
    title = models.CharField(max_length=200, help_text="The Name of the Service")
    featured_image = VersatileImageField(upload_to="Service/featured-images", blank=True, null=True,
                                         help_text="Service Background Image")
    mobile_image = VersatileImageField(upload_to='Gallery/mobile_images', blank=True, null=True,
                                       help_text="Mobile Image for hover image or carousel image")
    desktop_image = VersatileImageField(upload_to='Gallery/desktop_images', blank=True, null=True,
                                        help_text="Desktop Image for hover image or carousel image")
    icon_image = VersatileImageField(upload_to="Service/icon-images", blank=True, null=True,
                                     help_text="Service Icon Image")
    description = models.TextField(max_length=1000, blank=True, null=True, help_text="Service Description")
    sort_order = models.PositiveIntegerField(unique=True, help_text="Sort order to list the services")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('sort_order',)
