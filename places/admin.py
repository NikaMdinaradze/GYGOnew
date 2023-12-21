from django.contrib import admin
from .models import Place, Photo

# Register your models here.


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1  # Number of empty forms to display


class PlacesAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Place, PlacesAdmin)