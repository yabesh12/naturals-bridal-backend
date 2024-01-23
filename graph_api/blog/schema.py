import graphene
from graphene_django_pagination import DjangoPaginationConnectionField

from apps.blog.models import Blog
from graph_api.blog.type import BlogType


class BlogsQuery(graphene.ObjectType):
    get_blogs = DjangoPaginationConnectionField(BlogType,
                                                popular_blogs=graphene.Boolean(
                                                    description="Returns a list of Popular Blogs"),
                                                featured_blogs=graphene.Boolean(
                                                    description="Returns a list of Featured Blogs"),
                                                description="Returns a list of all Active Blogs")
    get_blog = graphene.Field(BlogType, slug=graphene.String(required=True),
                              description="Returns a Single Blog")

    def resolve_get_blogs(self, root, **kwargs):
        """
        :return: Returns all Active Blogs or all active popular blogs
        :param: popular_blogs (Optional:Bool Field)
        """
        popular_blogs = kwargs.get("popular_blogs", False)
        featured_blogs = kwargs.get("featured_blogs", False)
        query_dict = {"is_active": True}

        if popular_blogs:
            query_dict["is_popular_blog"] = True

        if featured_blogs:
            query_dict["is_featured"] = True

        return Blog.objects.filter(**query_dict)

    def resolve_get_blog(self, info, slug):
        """
        :return: Returns all Active Blogs
        """
        return Blog.objects.filter(slug=slug, is_active=True).first()
