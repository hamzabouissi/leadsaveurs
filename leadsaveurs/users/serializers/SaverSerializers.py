from rest_framework import serializers

from leadsaveurs.searcher.models import Mission
from leadsaveurs.users.models import Saver, User


class SaverMicroUserSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "role")


class SaverSerializerOut(serializers.ModelSerializer):
    user = SaverMicroUserSerializerOut()
    class Meta:
        model = Saver
        fields = ("id", "user")


class SaverMicroMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ("id", "name")


class SaverSerializerRetrieveOut(serializers.ModelSerializer):
    missions = SaverMicroMissionSerializer(many=True)
    user = SaverMicroUserSerializerOut()

    class Meta:
        model = Saver
        fields = ("id", "user", "missions_count","people_saved_count", "missions")


class SaverSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = Saver
        fields = ("id", "user")
