from django.contrib import admin

from apps.carousel.models import Carousel, CarouselItem


class CarouselItemInline(admin.StackedInline):
    model = CarouselItem
    extra = 2


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    """
    Custom Inline DjangoAdmin for Carousel Model
    """
    inlines = [CarouselItemInline]
    list_filter = ("carousel_type", "is_active")
    list_display = ("id", "title", "carousel_type", "sort_order")
    search_fields = ("id", "title", "carousel_type")
    ordering = ("-id",)
    fieldsets = (
        ('Standard Info', {
            'fields': (
                'carousel_type', 'title', 'sub_title', 'description', 'featured_image', 'mobile_image', 'desktop_image',
                'tags', 'hosted_video', 'provider', 'provider_url', 'sort_order', 'is_active', 'is_featured',)
        }),
        ('Artist Info', {
            'fields': ('date_of_birth', 'designation', 'specialised_style', 'is_travels_to_venue', 'years_of_exp',
                       'projects_completed',
                       'celebrity_projects')
        }),
        ('Magical Makeover Info', {
            'fields': ('before_mobile_image', 'before_desktop_image', 'after_mobile_image', 'after_desktop_image'),
        }),
        ('Other Info', {
            'fields': ('rating', 'redirect_url', 'published_at',
                       )
        }),
    )
