from .views import PlaceListAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", PlaceListAPIView, basename='place-list')

urlpatterns = [
    path('', include(router.urls)),
]