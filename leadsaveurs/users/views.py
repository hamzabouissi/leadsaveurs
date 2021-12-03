from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from leadsaveurs.core.Base import SerializerNone
from leadsaveurs.searcher.models import Donation
from leadsaveurs.users.models import Saver, UserSaved
from leadsaveurs.users.serializers.DonationSerializers import DonationSerializerOut, DonationSerializerIn
from leadsaveurs.users.serializers.SaverSerializers import SaverSerializerOut, SaverSerializerIn, \
    SaverSerializerRetrieveOut
from leadsaveurs.users.serializers.UserSavedSerializers import UserSavedSerializerIn, UserSavedSerializerOut
from leadsaveurs.users.serializers.UserSerializers import UserSerializerOut, UserSerializerIn, UserLoginSerializer
from leadsaveurs.users.services import authenticate_user

User = get_user_model()


# class UserDetailView(LoginRequiredMixin, DetailView):
#
#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"
#
#
# user_detail_view = UserDetailView.as_view()
#
#
# class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#
#     model = User
#     fields = ["name"]
#     success_message = _("Information successfully updated")
#
#     def get_success_url(self):
#         return self.request.user.get_absolute_url()  # type: ignore [union-attr]
#
#     def get_object(self):
#         return self.request.user
#
#
# user_update_view = UserUpdateView.as_view()


class UserViewSet(viewsets.ModelViewSet):
    serializers_class = {
        "create": UserSerializerIn,
        "list": UserSerializerOut,
        "retrieve":UserSerializerOut,
        "login": UserLoginSerializer
    }
    queryset = User.objects.all()

    # def get_queryset(self, *args, **kwargs):
    #     return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=["GET"],permission_classess=(IsAuthenticated,))
    def me(self, request):
        serializer = UserSerializerOut(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=["POST"], permission_classess=(AllowAny,))
    def login(self, request):
        ser = UserLoginSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = authenticate_user(ser.data['username'],ser.data['password'])
        if not user:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializerOut(user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class SaverView(viewsets.ModelViewSet):
    queryset = Saver.objects.all()
    serializers_class= {
        "list":SaverSerializerOut,
        "retrieve": SaverSerializerRetrieveOut,
        "create": SaverSerializerIn,
        "update": SaverSerializerIn,
    }

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)




class UserSavedView(viewsets.ModelViewSet):
    queryset = UserSaved.objects.all()
    serializers_class= {
        "list":UserSavedSerializerOut,
        "retrieve": UserSavedSerializerOut,
        "create": UserSavedSerializerIn,
        "update": UserSavedSerializerIn,
    }

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)


class DonationView(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializers_class = {
        "list": DonationSerializerOut,
        "retrieve": DonationSerializerOut,
        "create": DonationSerializerIn,
    }

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)
