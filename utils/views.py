from rest_framework import generics
from utils.serializers import TextSerializer, BannerSerializer
from utils.models import Text, Banner
# Create your views here.


class TextListView(generics.ListAPIView):
    serializer_class = TextSerializer
    queryset = Text.objects.all()
    ordering = ['id']


class BannerListView(generics.ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    ordering = ['id']
