import graphene

from graph_api.blog.schema import BlogsQuery
from graph_api.carousel.schema import CarouselQuery
from graph_api.contact_us.mutations import ContactUsMutation

# mutations by combining all the mutation classes
from graph_api.contact_us.schema import ContactUsQuery
from graph_api.gallery.schema import GalleryQuery
from graph_api.service.schema import ServicesQuery


class Mutations(
    ContactUsMutation,
    graphene.ObjectType):
    pass


# queries by combining all the query classes
class Queries(
    CarouselQuery,
    BlogsQuery,
    ServicesQuery,
    ContactUsQuery,
    GalleryQuery,
    graphene.ObjectType):
    pass


# schema by specifying the root query and mutations
schema = graphene.Schema(query=Queries, mutation=Mutations)
