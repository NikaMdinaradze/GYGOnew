from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import PlaceSerializer
from places.models import Place
from django_filters import rest_framework as filters
from places.filters import PlaceFilter


class PlaceListAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all().order_by('created_at')
    serializer_class = PlaceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlaceFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.views += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


