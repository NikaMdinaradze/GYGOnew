from .views import PlaceListAPIView
from django.urls import path

urlpatterns = [
    path('', PlaceListAPIView.as_view()),
]