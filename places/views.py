from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response

from places.filters import PlaceFilter
from places.models import Place

from .serializers import PlaceSerializer


class PlaceListAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all().order_by("created_at")
    serializer_class = PlaceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlaceFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.views += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        # Prefetch related photos to reduce database queries
        queryset = queryset.prefetch_related("photos")
        return queryset
