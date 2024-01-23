import graphene
from graphene_django import DjangoObjectType
from apps.gallery.models import Gallery, GalleryItem


class GalleryType(DjangoObjectType):
    """
    Graphene DjangoObjectType for Gallery Model
    """
    featured_image_url = graphene.String(description="Featured Image's URL")
    mobile_image_url = graphene.String(description="Mobile Image Url Link")
    desktop_image_url = graphene.String(description="Desktop Image Url Link")
    hosted_video_url = graphene.String(description="Self hosted video URL")
    icon_image_url = graphene.String(description="Icon Image Url Link")

    class Meta:
        model = Gallery
        exclude = (
            "created_at", "updated_at", "featured_image", "mobile_image", "desktop_image", "icon_image", "is_active",
            "hosted_video")
        interfaces = (graphene.relay.Node,)

    def resolve_featured_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(
            self.featured_image.url) if self.featured_image else None

    def resolve_hosted_video_url(self, info):
        """
        used to change relative path of the file to absolute path
        """
        return info.context.build_absolute_uri(self.hosted_video.url) if self.hosted_video else None

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


class GalleryItemType(DjangoObjectType):
    """
    Graphene DjangoObjectType for GalleryItem Model
    """
    mobile_image_url = graphene.String(description="Mobile Image Url Link")
    desktop_image_url = graphene.String(description="Desktop Image Url Link")

    class Meta:
        model = GalleryItem
        exclude = ("created_at", "updated_at", "mobile_image", "desktop_image", "hosted_video")
        interfaces = (graphene.relay.Node,)

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
