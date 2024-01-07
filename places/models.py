from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='photos/')

    monday_open = models.TimeField(null=True, blank=True)
    monday_close = models.TimeField(null=True, blank=True)

    tuesday_open = models.TimeField(null=True, blank=True)
    tuesday_close = models.TimeField(null=True, blank=True)

    wednesday_open = models.TimeField(null=True, blank=True)
    wednesday_close = models.TimeField(null=True, blank=True)

    thursday_open = models.TimeField(null=True, blank=True)
    thursday_close = models.TimeField(null=True, blank=True)

    friday_open = models.TimeField(null=True, blank=True)
    friday_close = models.TimeField(null=True, blank=True)

    saturday_open = models.TimeField(null=True, blank=True)
    saturday_close = models.TimeField(null=True, blank=True)

    sunday_open = models.TimeField(null=True, blank=True)
    sunday_close = models.TimeField(null=True, blank=True)

    description = models.TextField()
    district = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255)

    number = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.URLField(null=True, max_length=255, blank=True)
    instagram = models.URLField(null=True, max_length=255, blank=True)
    tiktok = models.URLField(null=True, max_length=255, blank=True)
    youtube = models.URLField(null=True, max_length=255, blank=True)
    discord = models.URLField(null=True, max_length=255, blank=True)
    telegram = models.URLField(null=True, max_length=255, blank=True)

    main_price = models.IntegerField()
    main_visit = models.CharField(max_length=255)
    custom_price = models.CharField(max_length=255, null=True, blank=True)
    map_link = models.URLField(max_length=255)
    views = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    place = models.ForeignKey(Place, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
