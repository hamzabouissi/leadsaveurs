from rest_framework import serializers

from leadsaveurs.users.models import UserSaved
from leadsaveurs.searcher.models import Mission


class MissionMicroSavedUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSaved
        fields = ("id", "user")


class MissionMicroSaverUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSaved
        fields = ("id", "user", "grade")


class MissionSerializerOut(serializers.ModelSerializer):
    saved_users = MissionMicroSavedUsersSerializer(many=True)
    savers = MissionMicroSaverUserSerializer(many=True)
    captain = MissionMicroSaverUserSerializer()

    class Meta:
        model = Mission
        fields = ("id", "name", "boat", "captain", "saved_users", "savers", "start_date", "end_date", "start_location",
                  "end_location", "status", "is_missing")


class MissionSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ("id", "name", "boat", "captain", "start_date", "end_date", "start_location", "end_location")
