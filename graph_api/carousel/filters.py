import django_filters
from django.db.models import Q

from apps.carousel.models import Carousel
from graph_api.carousel.utils import TaggableManagerFilter


class CarouselFilter(django_filters.FilterSet):
    """
    Custom Filter for Carousel Object Type
    """
    tags = TaggableManagerFilter(field_name='tags', lookup_expr='exact')
    is_travels_to_venue = django_filters.BooleanFilter(field_name='is_travels_to_venue')
    specialised_style = django_filters.CharFilter(field_name='specialised_style', lookup_expr='exact')
    search = django_filters.CharFilter(method='perform_search')

    class Meta:
        model = Carousel
        fields = ['tags', 'is_travels_to_venue', 'specialised_style', 'search']

    def perform_search(self, queryset, name, value):
        """
        Used for search in carousel
        """
        qs = queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value) |
            Q(specialised_style__icontains=value) |
            Q(sub_title__icontains=value) |
            Q(tags__name__icontains=value)
        )
        return qs if qs.exists() else queryset.all()
