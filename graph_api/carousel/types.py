from datetime import date

import graphene
from graphene_django import DjangoObjectType

from apps.carousel.models import Carousel, CarouselItem
from graph_api.carousel.filters import CarouselFilter


class CarouselType(DjangoObjectType):
    """
    Graphene DjangoObjectType for Carousel Model
    """
    featured_image_url = graphene.String(description="Carousel Featured Image URL")
    hosted_video_url = graphene.String(description="Hosted Video Url Link")
    mobile_image_url = graphene.String(description="Mobile Image Url Link")
    desktop_image_url = graphene.String(description="Desktop Image Url Link")
    before_makeup_mobile_image_url = graphene.String(description="Before Makeup Mobile Image Url Link")
    before_makeup_desktop_image_url = graphene.String(description="Before Makeup Desktop Image Url Link")
    after_makeup_mobile_image_url = graphene.String(description="After Makeup Mobile Image Url Link")
    after_makeup_desktop_image_url = graphene.String(description="After Makeup Desktop Image Url Link")
    age = graphene.Int(description="Returns Artist/Person Age from DOB")
    icon_image_url = graphene.String(description="Icon Image Url Link")

    class Meta:
        model = Carousel
        exclude = (
            "created_at", "updated_at", "is_active", "featured_image", "mobile_image", "desktop_image", "icon_image",
            "before_mobile_image", "before_desktop_image",
            "after_mobile_image", "after_desktop_image",
            "hosted_video",)
        filterset_class = CarouselFilter
        interfaces = (graphene.relay.Node,)

    def resolve_featured_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.featured_image.url) if self.featured_image else None

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

    def resolve_before_makeup_mobile_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.before_mobile_image.url) if self.before_mobile_image else None

    def resolve_before_makeup_desktop_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.before_desktop_image.url) if self.before_desktop_image else None

    def resolve_after_makeup_mobile_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.after_mobile_image.url) if self.after_mobile_image else None

    def resolve_after_makeup_desktop_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.after_desktop_image.url) if self.after_desktop_image else None

    def resolve_age(self, info):
        """
        Get age from DOB
        """
        today = date.today()
        if self.date_of_birth:
            age = today.year - self.date_of_birth.year
            # Check if the birthday has already occurred this year
            if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
                age -= 1
            return age
        return None

    def resolve_icon_image_url(self, info):
        """
        used to change relative path of the image to absolute path
        """
        return info.context.build_absolute_uri(self.icon_image.url) if self.icon_image else None


class CarouselItemType(DjangoObjectType):
    """
    Graphene DjangoObjectType for CarouselItem Model
    """
    mobile_image_url = graphene.String(description="Carousel Mobile Image URL")
    desktop_image_url = graphene.String(description="Carousel Desktop Image URL")
    hosted_video_url = graphene.String(description="Hosted Video Url Link")
    portfolio_mobile_image_url = graphene.String(description="Portfolio Mobile Image URL")
    portfolio_desktop_image_url = graphene.String(description="Portfolio Desktop Image URL")

    class Meta:
        model = CarouselItem
        exclude = ("created_at", "updated_at", "mobile_image", "desktop_image", "portfolio_mobile_image", "portfolio_desktop_image", "hosted_video")
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

    def resolve_hosted_video_url(self, info):
        """
        used to change relative path of the file to absolute path
        """
        return info.context.build_absolute_uri(self.hosted_video.url) if self.hosted_video else None

    def resolve_portfolio_mobile_image_url(self, info):
        """
        used to change relative path of the file to absolute path
        """
        return info.context.build_absolute_uri(self.portfolio_mobile_image.url) if self.portfolio_mobile_image else None

    def resolve_portfolio_desktop_image_url(self, info):
        """
        used to change relative path of the file to absolute path
        """
        return info.context.build_absolute_uri(self.portfolio_desktop_image.url) if self.portfolio_desktop_image else None