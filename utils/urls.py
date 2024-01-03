from utils.views import TextListView, BannerListView
from django.urls import path


urlpatterns = [
    path('text/', TextListView.as_view()),
    path('banner/', BannerListView.as_view()),
]
