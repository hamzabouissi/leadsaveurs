from rest_framework import serializers

from leadsaveurs.searcher.models import Mission
from leadsaveurs.users.models import UserSaved

class UserSavedMicroMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ("id", "name")


class UserSavedSerializerOut(serializers.ModelSerializer):
    missions = UserSavedMicroMissionSerializer(many=True)

    class Meta:
        model = UserSaved
        fields = ("id", "user" ,"missions_count", "missions")


class UserSavedSerializerIn(serializers.ModelSerializer):

    class Meta:
        model = UserSaved
        fields = ("id", "user")
