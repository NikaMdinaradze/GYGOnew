from rest_framework import serializers

from .models import Photo, Place


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("image",)


class PlaceSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = (
            "id",
            "name",
            "category",
            "logo",
            "monday_open",
            "monday_close",
            "tuesday_open",
            "tuesday_close",
            "wednesday_open",
            "wednesday_close",
            "thursday_open",
            "thursday_close",
            "friday_open",
            "friday_close",
            "saturday_open",
            "saturday_close",
            "sunday_open",
            "sunday_close",
            "description",
            "district",
            "full_address",
            "number",
            "facebook",
            "instagram",
            "tiktok",
            "youtube",
            "discord",
            "telegram",
            "main_price",
            "main_visit",
            "custom_price",
            "map_link",
            "views",
            "photos",
        )
