import graphene
from graphene_django_pagination import DjangoPaginationConnectionField

from apps.carousel.models import Carousel
from graph_api.carousel.enum import CarouselFilterEnum
from graph_api.carousel.types import CarouselType


class CarouselQuery(graphene.ObjectType):
    get_carousels = DjangoPaginationConnectionField(CarouselType,
                                                    description="Returns a list of specific carousel and it's images based on specific Carousel Enum",
                                                    carousel_enum=CarouselFilterEnum(description="The Carousel Enum"))
    get_carousel_item = graphene.relay.Node.Field(CarouselType, description="Get specific Carousel's Items")

    def resolve_get_carousels(self, root, **kwargs):
        """
        Returns a specific Carousel and its images based on carousel_enum
        """
        carousel_enum = kwargs.get("carousel_enum")
        filter_dict = {"is_active": True}
        if carousel_enum:
            filter_dict["carousel_type"] = carousel_enum.name
        return Carousel.objects.filter(**filter_dict)
