from django.db import models


class Text(models.Model):
    PRODUCT = 'product'
    SEARCH = 'search'
    HOME = 'home'

    TYPE_CHOICES = [
        (PRODUCT, 'Product'),
        (SEARCH, 'Search'),
        (HOME, 'Home'),
    ]

    text = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)


class Banner(models.Model):
    image = models.ImageField(upload_to="photos/")
    company = models.CharField(max_length=255)
