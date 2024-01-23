import graphene
from graphql import GraphQLError

from apps.gallery.models import Gallery
from graph_api.gallery.enum import GalleryFilterEnum
from graph_api.gallery.types import GalleryType


class GalleryQuery(graphene.ObjectType):
    get_gallery = graphene.List(GalleryType,
                                description="Returns a list of specific gallery images based on specific Gallery Enum",
                                gallery_enum=GalleryFilterEnum(required=True, description="The Gallery Enum"))
    get_gallery_items = graphene.relay.Node.Field(GalleryType,
                                                  description="Returns a list of Specific Gallery and it's Items")

    def resolve_get_gallery(self, root, gallery_enum, **kwargs):
        """
        Returns a specific Gallery and its images based on gallery_enum
        """
        filter_dict = {}
        match gallery_enum.name:
            case "BRIDAL_SERVICE_GALLERY":
                filter_dict.update({'gallery_type': gallery_enum.name, 'is_active': True})

            case "CLIENT_GALLERY":
                filter_dict.update({'gallery_type': gallery_enum.name, 'is_active': True})

            case default:
                raise GraphQLError("Gallery not Found!")
        return Gallery.objects.filter(**filter_dict)
