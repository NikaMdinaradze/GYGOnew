from django.contrib import admin
from .models import Text, Banner


class TextAdmin(admin.ModelAdmin):
    list_display = ('text', 'type', 'created_at')
    # Add any other customizations you want


admin.site.register(Text, TextAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('image', 'company', 'created_at')
    # Add any other customizations you want


admin.site.register(Banner, BannerAdmin)
