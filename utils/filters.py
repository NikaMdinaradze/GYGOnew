from django_filters import rest_framework as filters
from utils.models import Text


class TextFilter(filters.FilterSet):
    type = filters.ChoiceFilter(choices=Text.TYPE_CHOICES)

    class Meta:
        model = Text
        fields = ['type']