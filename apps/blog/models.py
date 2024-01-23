import math
import readtime
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager
from versatileimagefield.fields import VersatileImageField
from django_editorjs_fields import EditorJsJSONField
from apps.core.models import TimestampModel


class Blog(TimestampModel):
    title = models.CharField(max_length=100, help_text="The Blog Title", unique=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True, help_text="Blog's Meta Title")
    meta_description = models.CharField(max_length=100, blank=True, null=True, help_text="Blog's Meta Description")
    short_description = models.CharField(max_length=100, blank=True, null=True, help_text="Blog's Short Description")
    sub_description = models.TextField(max_length=300, blank=True, null=True, help_text="Blog Sub Description")
    description = models.TextField(max_length=10000, help_text="Blog Content This field is deprecated")
    body = EditorJsJSONField(
        verbose_name='Blog Content',
        blank=True,
        null=True,
    )
    featured_image_mobile = VersatileImageField("Thumbnail Image Mobile", help_text="Background image for mobile")
    featured_image_desktop = VersatileImageField("Thumbnail Image Desktop", help_text="Background image for desktop")
    main_image_mobile = VersatileImageField("Main Image Mobile", blank=True, null=True,
                                            help_text="Main image for mobile")
    main_image_desktop = VersatileImageField("Main Image Desktop", blank=True, null=True,
                                             help_text="Main image for desktop")
    tags = TaggableManager(blank=True)
    published_at = models.DateField(auto_now_add=True, help_text="Published Date")
    read_time = models.PositiveIntegerField(default=0,
                                            help_text="The Blog read time automatically calculated after save")
    is_featured = models.BooleanField(default=False, help_text="Featured Blog?")
    is_popular_blog = models.BooleanField(default=False, help_text="Popular Blog?")
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(help_text="List the Blogs based on sort order")
    slug = models.SlugField(help_text="The slug for the current blog")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("sort_order",)
        unique_together = ('is_featured', 'sort_order')

    def clean(self):
        # validate Image Upload
        if self.featured_image_mobile and not self.featured_image_desktop:
            raise ValidationError("Please provide featured desktop image")
        if self.featured_image_desktop and not self.featured_image_mobile:
            raise ValidationError("Please provide featured mobile image")
        # validate sort order for active blogs
        if not self.is_featured:
            if Blog.objects.filter(sort_order=self.sort_order, is_featured=False).exclude(id=self.id).exists():
                raise ValidationError("Sort Order already exists!")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # to calculate the blog read time
        if self.description:
            readtime_min = readtime.of_text(self.description, wpm=80)
            self.read_time = round(math.ceil(readtime_min.seconds / 60))

        # Generate the slug from the title
        self.slug = slugify(self.title)
        super(Blog, self).save()
