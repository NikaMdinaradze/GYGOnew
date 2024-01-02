from django_filters import rest_framework as filters
from places.models import Place


class PlaceFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="main_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="main_price", lookup_expr='lte')

    class Meta:
        model = Place
        fields = ("name", "category", "full_address")
