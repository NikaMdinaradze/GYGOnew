from .serializers import PlaceSerializer
from rest_framework.generics import ListAPIView
from .models import Place
from django.db.models import Q
from rest_framework.filters import SearchFilter


class PlaceListAPIView(ListAPIView):
    serializer_class = PlaceSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'category', 'full_address']

    def get_queryset(self):
        queryset = Place.objects.prefetch_related('photos').all().order_by('created_at')

        # Filtering
        category = self.request.query_params.get('category', None)
        district = self.request.query_params.get('district', None)
        max_price = self.request.query_params.get('max_price', None)
        min_price = self.request.query_params.get('min_price', None)

        if category:
            queryset = queryset.filter(category=category)
        if district:
            queryset = queryset.filter(district=district)
        if max_price:
            queryset = queryset.filter(main_price__lte=max_price)
        if min_price:
            queryset = queryset.filter(main_price__gte=min_price)

        return queryset
