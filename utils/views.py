from rest_framework import generics
from utils.serializers import TextSerializer, BannerSerializer
from utils.models import Text, Banner
from django_filters import rest_framework as filters
from utils.filters import TextFilter
# Create your views here.


class TextListView(generics.ListAPIView):
    serializer_class = TextSerializer
    queryset = Text.objects.all()
    ordering = ['id']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TextFilter


class BannerListView(generics.ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    ordering = ['id']
