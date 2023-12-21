from rest_framework import serializers
from .models import Place, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "image",


class PlaceSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Place
        fields = "description", "photos"

