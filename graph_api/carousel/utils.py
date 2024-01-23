import django_filters
from graphene import List, String
from graphene_django.converter import convert_django_field
from taggit.managers import TaggableManager


@convert_django_field.register(TaggableManager)
def convert_field_to_string(field, registry=None):
    """
    Converts a TaggableManager field into a list of strings for GraphQL schema
    """
    return List(String, source='get_tags')


class TaggableManagerFilter(django_filters.CharFilter):
    """
    Custom Filter for Tags
    """

    def filter(self, qs, value):
        if value:
            tags = value.split(",")
            return qs.filter(tags__name__in=tags)
        return qs
