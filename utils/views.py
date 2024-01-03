from rest_framework import generics
from utils.serializers import TextSerializer
from utils.models import Text
# Create your views here.


class TextListView(generics.ListAPIView):
    serializer_class = TextSerializer
    queryset = Text.objects.all()
    ordering = ['id']
