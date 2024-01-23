from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from taggit.managers import TaggableManager
from versatileimagefield.fields import VersatileImageField

from apps.core.models import TimestampModel
from apps.core.utils import validate_image, validate_video, validate_video_upload

VIDEO_PROVIDER_CHOICES = (
    ("YOUTUBE", "YOUTUBE"),
    ("FACEBOOK", "FACEBOOK"),
    ("INSTAGRAM", "INSTAGRAM"),
    ("VIMEO", "VIMEO"),
)

CAROUSEL_TYPE = (
    ("_90_DAYS_JOURNEY", "90 DAYS JOURNEY"),
    ("MAGICAL_MAKEOVER", "MAGICAL MAKEOVER"),
    ("SERVICES_BANNER", "SERVICES BANNER"),
    ("MAKEUP_VARIATIONS", "MAKEUP VARIATIONS"),
    ("TOP_MAKEUP_ARTISTS", "TOP MAKEUP ARTISTS"),
    ("SPECIALTY_MAKEUP_ARTISTS", "SPECIALTY MAKEUP ARTISTS"),
    ("CLIENT_TESTIMONIALS", "CLIENT TESTIMONIALS"),
    ("BRAND_PARTNERS", "BRAND PARTNERS"),
)


class Carousel(TimestampModel):
    carousel_type = models.CharField(max_length=200, choices=CAROUSEL_TYPE, help_text="Type of carousel", blank=True,
                                     null=True)
    title = models.CharField("Title/Name", max_length=100, blank=True, null=True, help_text="Carousel Name")
    sub_title = models.CharField(max_length=60, blank=True, null=True, help_text="Carousel subtext")
    description = models.TextField(max_length=1000, help_text="Carousel Description", blank=True, null=True)
    # For Artists
    date_of_birth = models.DateField(blank=True, null=True, help_text="date of birth of the Artist/Person")
    specialised_style = models.CharField(max_length=60, blank=True, null=True, help_text="Style Speciality")
    tags = TaggableManager(blank=True)
    designation = models.CharField(max_length=50, blank=True, null=True, help_text="Client's Designation")
    is_travels_to_venue = models.BooleanField(default=True, help_text="Artist availability for travel")
    years_of_exp = models.PositiveIntegerField("Total Years of Experience", default=0,
                                               help_text="Artist's Years of Experience")
    projects_completed = models.PositiveIntegerField(default=0, help_text="Total Projects Completed by Artist")
    celebrity_projects = models.PositiveIntegerField(default=0,
                                                     help_text="Total Celebrity Projects Completed by Artist")
    rating = models.PositiveIntegerField(blank=True, null=True, help_text="Rating Number")
    featured_image = VersatileImageField(upload_to="Carousel/featured_images", blank=True, null=True,
                                         help_text="Carousel background image")
    icon_image = VersatileImageField(upload_to="Carousel/icon_images", blank=True, null=True,
                                         help_text="Carousel Icon image")
    mobile_image = VersatileImageField(upload_to='Carouse/mobile_images', blank=True, null=True,
                                       help_text="Upload Image for Mobile")
    desktop_image = VersatileImageField(upload_to='Carouse/desktop_images', blank=True, null=True,
                                        help_text="Upload Image for Desktop")
    # MAGICAL MAKEOVER SECTION
    before_mobile_image = VersatileImageField(upload_to='Carouse/Magical_Makeover/mobile_images', blank=True, null=True,
                                              help_text="Upload Mobile Image for before Makeup")
    before_desktop_image = VersatileImageField(upload_to='Carouse/Magical_Makeover/desktop_images', blank=True,
                                               null=True,
                                               help_text="Upload Desktop Image for before Makeup")
    after_mobile_image = VersatileImageField(upload_to='Carouse/Magical_Makeover/mobile_images', blank=True, null=True,
                                             help_text="Upload Mobile Image for after Makeup")
    after_desktop_image = VersatileImageField(upload_to='Carouse/Magical_Makeover/desktop_images', blank=True,
                                              null=True,
                                              help_text="Upload Desktop Image for after Makeup")
    # VIDEO FIELDS
    hosted_video = models.FileField(upload_to='Carousel/videos', max_length=200, null=True, blank=True,
                                    help_text="Video upload file")
    provider = models.CharField(max_length=100, choices=VIDEO_PROVIDER_CHOICES, null=True, blank=True,
                                help_text="Video provider name")
    provider_url = models.URLField(max_length=300, null=True, blank=True, help_text="Video URL")
    redirect_url = models.URLField(max_length=300, null=True, blank=True, help_text="used for Redirect URL")
    sort_order = models.PositiveIntegerField(unique=True, blank=True, null=True,
                                             help_text="The Sort Order for the Carousel")
    published_at = models.DateField(blank=True, null=True, help_text="Carousel Published date")
    is_active = models.BooleanField(default=True, help_text="Carousel Status")
    is_featured = models.BooleanField(default=False, help_text="Featured Carousel")

    class Meta:
        verbose_name_plural = 'Carousels'
        ordering = ("sort_order",)
        unique_together = ('carousel_type', 'sort_order')

    def __str__(self):
        return self.title if self.title is not None else self.carousel_type

    def clean(self):
        validate_video_upload(self.hosted_video, self.provider_url, self.provider)
        validate_video(0 if not self.hosted_video else self.hosted_video.size)
        validate_image([0 if not self.featured_image else self.featured_image.size,
                        0 if not self.mobile_image else self.mobile_image.size,
                        0 if not self.desktop_image else self.desktop_image.size,
                        0 if not self.after_mobile_image else self.after_mobile_image.size,
                        0 if not self.after_desktop_image else self.after_desktop_image.size,
                        0 if not self.before_mobile_image else self.before_mobile_image.size,
                        0 if not self.before_desktop_image else self.before_desktop_image.size
                        ])

        # Perform age validation
        if self.date_of_birth:
            if self.date_of_birth > date.today():
                raise ValidationError("Date of birth cannot be a future or current date.")
            return None

    @property
    def get_tags(self):
        return self.tags.all()


class CarouselItem(TimestampModel):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE, related_name='carousel_items')
    brand_name = models.CharField(max_length=100, help_text='Provide Brand Name', blank=True, null=True)
    mobile_image = VersatileImageField('Carousel Item Mobile Image', upload_to='Carousel/pics',
                                       help_text="Hover/Carousel Mobile Image", blank=True, null=True)
    desktop_image = VersatileImageField('Carousel Item Desktop Image', upload_to='Carousel/pics',
                                        help_text="Hover/Carousel Desktop Image", blank=True, null=True)
    portfolio_mobile_image = VersatileImageField('Portfolio Carousel Item Mobile Image', upload_to='Carousel/portfolio/pics',
                                        help_text="Hover/Portfolio Carousel Mobile Image", blank=True, null=True)
    portfolio_desktop_image = VersatileImageField('Portfolio Carousel Item Desktop Image', upload_to='Carousel/portfolio/pics',
                                        help_text="Hover/Portfolio Carousel Desktop Image", blank=True, null=True)
    hosted_video = models.FileField(upload_to='Carousel/videos', max_length=200, null=True, blank=True,
                                    help_text="Video upload file")
    provider = models.CharField(max_length=100, choices=VIDEO_PROVIDER_CHOICES, null=True, blank=True,
                                help_text="Video provider name")
    provider_url = models.URLField(max_length=300, null=True, blank=True, help_text="Video URL")
    sort_order = models.PositiveIntegerField(blank=True, null=True,
                                             help_text="The Sort Order for the Carousel Item")

    class Meta:
        verbose_name_plural = 'Carousel Images'
        ordering = ("-id",)
        unique_together = ("carousel", "sort_order")

    def __str__(self):
        return self.carousel.title

    def clean(self):
        validate_video_upload(self.hosted_video, self.provider_url, self.provider)
        validate_video(0 if not self.hosted_video else self.hosted_video.size)
        validate_image([self.mobile_image.size, self.desktop_image.size])

        return None
