from django.contrib import admin
from apps.blog.models import Blog
from apps.blog.resources import BlogResource


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Custom DjangoAdmin for Blog Model
    """
    resource_class = BlogResource
    list_filter = ("is_active", "is_featured", "title", "published_at",)
    list_display = ("id", "title", "sort_order", "read_time", "is_featured", "published_at")
    search_fields = ("id", "title", "is_featured", "read_time", "published_at")
    readonly_fields = ("published_at", "read_time", "slug")
    list_editable = ("title", "sort_order", "read_time", "is_featured")
    ordering = ("-id",)
    # date-hierarchy
    date_hierarchy = 'created_at'
    date_hierarchy_drilldown = False
