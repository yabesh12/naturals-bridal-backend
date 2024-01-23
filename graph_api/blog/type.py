import graphene
from graphene_django import DjangoObjectType

from apps.blog.models import Blog
from graph_api.blog.filters import BlogFilter


class BlogType(DjangoObjectType):
    """
    Graphene DjangoObjectType for Blog Model
    """
    featured_image_mobile_url = graphene.String(description="Background Image Url for Mobile")
    featured_image_desktop_url = graphene.String(description="Background Image Url for Desktop")
    main_image_mobile_url = graphene.String(description="Main Image Url for Mobile")
    main_image_desktop_url = graphene.String(description="Main Image Url for Desktop")

    class Meta:
        model = Blog
        exclude = (
            "created_at", "updated_at", "is_active", "featured_image_mobile", "featured_image_desktop",
            "main_image_mobile", "main_image_desktop")
        interfaces = (graphene.relay.Node,)
        filterset_class = BlogFilter

    def resolve_featured_image_mobile_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(
            self.featured_image_mobile.url) if self.featured_image_mobile else None

    def resolve_featured_image_desktop_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(
            self.featured_image_desktop.url) if self.featured_image_desktop else None

    def resolve_main_image_mobile_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.main_image_mobile.url) if self.main_image_mobile else None

    def resolve_main_image_desktop_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.main_image_desktop.url) if self.main_image_desktop else None
