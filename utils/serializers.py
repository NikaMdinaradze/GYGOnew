from utils.models import Text, Banner
from rest_framework import serializers


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('text', 'type',)


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('image', 'company',)

