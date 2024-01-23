from django.contrib import admin
from apps.gallery.models import Gallery, GalleryItem, TimestampModel


class GalleryItemInline(admin.StackedInline):
    model = GalleryItem
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """s
    Custom DjangoAdmin for Gallery Model
    """
    inlines = [GalleryItemInline]
    list_filter = ("gallery_type",)
    list_display = ("id", "name", "gallery_type")
    search_fields = ("id", "name", "gallery_type")
    ordering = ("-id",)
    fieldsets = (
        ('Standard Info', {
            'fields': ('gallery_type', 'name', 'description', 'featured_image', 'mobile_image', 'desktop_image', 'hosted_video', 'provider', 'provider_url', 'is_active')
        }),
    )
