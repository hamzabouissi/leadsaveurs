from rest_framework import serializers

from leadsaveurs.users.models import User


class HomeSearchSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "role")
