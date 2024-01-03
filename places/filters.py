from django_filters import rest_framework as filters
from places.models import Place
from django.db import models

class PlaceFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="main_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="main_price", lookup_expr='lte')
    search = filters.CharFilter(method='custom_search_filter')

    class Meta:
        model = Place
        fields = ("category", "district")

    def custom_search_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__icontains=value) |
            models.Q(full_address__icontains=value) |
            models.Q(category__icontains=value)
        )
