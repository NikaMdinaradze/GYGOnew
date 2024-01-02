from .serializers import PlaceSerializer
from rest_framework.generics import ListAPIView
from places.models import Place
from django_filters import rest_framework as filters
from places.filters import PlaceFilter


class PlaceListAPIView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlaceFilter

