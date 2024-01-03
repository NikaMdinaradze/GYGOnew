from utils.views import TextListView
from django.urls import path


urlpatterns = [
    path('text/', TextListView.as_view()),
]