from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from leadsaveurs.core.Base import SerializerNone
from leadsaveurs.searcher.filters import HomeSearchViewFilter
from leadsaveurs.searcher.models import Mission, MissionReclamation, Donation
from leadsaveurs.searcher.serializers.MissionSerializers import MissionSerializerOut, MissionSerializerIn
from leadsaveurs.searcher.serializers.SearchSerialziers import HomeSearchSerializerOut
from leadsaveurs.users.models import Saver, User, UserRoleEnum
from rest_framework.generics import GenericAPIView, ListAPIView

from leadsaveurs.users.serializers.DonationSerializers import DonationSerializerOut
from leadsaveurs.users.serializers.MissionReclamationSerializers import MissionReclamationSerializerIn, \
    MissionReclamationSerializerOut

class HomeSearchView(ListAPIView):
    queryset = User.objects.filter(role__in=[UserRoleEnum.UserSaved, UserRoleEnum.Saver])
    serializer_class = HomeSearchSerializerOut
    filter_backends = [DjangoFilterBackend]
    filterset_class = HomeSearchViewFilter
    permission_classes = (AllowAny,)


class MissionView(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializers_class = {
        "list": MissionSerializerOut,
        "retrieve": MissionSerializerOut,
        "create": MissionSerializerIn,
        "update": MissionSerializerIn,
    }

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)


class MissionReclamationView(viewsets.ModelViewSet):
    queryset = MissionReclamation.objects.all()
    serializers_class = {
        "list": MissionReclamationSerializerOut,
        "retrieve": MissionReclamationSerializerOut,
        "create": MissionReclamationSerializerIn,
        "update": MissionReclamationSerializerIn,
    }

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)


class DonationView(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializers_class = {
        "list": DonationSerializerOut,
        "retrieve": MissionSerializerOut,
        "create": MissionSerializerIn,
        "update": MissionSerializerIn,
    }

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)
