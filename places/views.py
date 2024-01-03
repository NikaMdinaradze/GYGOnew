from .serializers import PlaceSerializer
from rest_framework import viewsets
from places.models import Place
from django_filters import rest_framework as filters
from places.filters import PlaceFilter


class PlaceListAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlaceFilter

