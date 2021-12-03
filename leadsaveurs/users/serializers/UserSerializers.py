from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from leadsaveurs.users.models import User, UserRoleEnum


class UserSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "name"]




class UserSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "name", "email", "password", "role", "location","phone"]

    def validate_password(self,value):
        return make_password(value)

    def create(self, validated_data):

        role = validated_data['role']
        if role == UserRoleEnum.Saver:
            Saver()


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","password")
