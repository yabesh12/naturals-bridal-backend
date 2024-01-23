import django_filters
from django.db.models import Q

from apps.blog.models import Blog
from graph_api.carousel.utils import TaggableManagerFilter


class BlogFilter(django_filters.FilterSet):
    """
    Custom Filter for Blog Object Type
    """
    tags = TaggableManagerFilter(field_name='tags', lookup_expr='exact')
    search = django_filters.CharFilter(method='perform_search')

    class Meta:
        model = Blog
        fields = ['tags', 'search']

    def perform_search(self, queryset, name, value):
        """
        Used for search in carousel
        """
        qs = queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value) |
            Q(tags__name__icontains=value)
        )

        return qs if qs.exists() else queryset.all()
