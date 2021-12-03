from django_filters import rest_framework as filters

from leadsaveurs.users.models import User


class HomeSearchViewFilter(filters.FilterSet):

    class Meta:
        model = User
        fields = ("name",)
