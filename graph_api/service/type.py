import graphene
from graphene_django import DjangoObjectType

from apps.service.models import Service


class ServiceType(DjangoObjectType):
    """
    Graphene DjangoObjectType for Service Model
    """
    featured_image_url = graphene.String(description="Featured Image Url Link")
    mobile_image_url = graphene.String(description="Mobile Image Url Link")
    desktop_image_url = graphene.String(description="Desktop Image Url Link")
    icon_image_url = graphene.String(description="Icon Image Url Link")

    class Meta:
        model = Service
        exclude = (
        "created_at", "updated_at", "featured_image", "mobile_image", "desktop_image", 'icon_image', "is_active")
        interfaces = (graphene.relay.Node,)

    def resolve_featured_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.featured_image.url) if self.featured_image else None

    def resolve_mobile_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.mobile_image.url) if self.mobile_image else None

    def resolve_desktop_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.desktop_image.url) if self.desktop_image else None

    def resolve_icon_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.icon_image.url) if self.icon_image else None
