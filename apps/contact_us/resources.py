from import_export import resources

from apps.contact_us.models import ContactEnquiry


class ContactUsResource(resources.ModelResource):
    """
    Resource Class for Model ContactUs
    """

    def get_export_headers(self):
        super().get_export_headers()
        new_headers = ['id', 'Submitted At', 'First Name', 'Last Name', 'Email', 'Contact Number', 'Service', 'Artist',
                       'Message', 'Enquiry Type']
        return new_headers

    class Meta:
        model = ContactEnquiry
        fields = (
        'id', 'created_at', 'first_name', 'last_name', 'email', 'phone_number', 'service__title', 'artist__title',
        'message', 'enquiry_type')
        export_order = (
        'id', 'created_at', 'first_name', 'last_name', 'email', 'phone_number', 'service__title', 'artist__title',
        'message', 'enquiry_type')
