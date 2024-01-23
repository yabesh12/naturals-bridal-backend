from import_export import resources
from import_export.admin import ImportExportMixin

from apps.blog.models import Blog


class BlogResource(ImportExportMixin, resources.ModelResource):
    """
    Resource Class for Model Blog
    """

    class Meta:
        model = Blog
        fields = "__all__"
