from django.contrib import admin
from import_export.admin import ExportMixin

from apps.contact_us.models import ContactEnquiry, Address
from apps.contact_us.resources import ContactUsResource


@admin.register(ContactEnquiry)
class ContactUsAdmin(ExportMixin, admin.ModelAdmin):
    """
    Custom DjangoAdmin for ContactUs Model
    """
    resource_class = ContactUsResource
    list_filter = ("enquiry_type", "artist", "service")
    list_display = ("id", "service", "artist", "enquiry_type", "email", "phone_number")
    search_fields = ("id", "service", "email", "phone_number")
    ordering = ("-id",)
    # date-hierarchy
    date_hierarchy = 'created_at'
    date_hierarchy_drilldown = False


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
    Custom DjangoAdmin for Address Model
    """
    list_filter = ("state", "city", "country")
    list_display = ("id", "address_line1", "email", "state", "city", "country")
    search_fields = ("id", "address_line1", "email", "phone_number", "state", "city")
    ordering = ("-id",)
