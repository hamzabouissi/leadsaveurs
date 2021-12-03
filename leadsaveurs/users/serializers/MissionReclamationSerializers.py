from rest_framework import serializers

from leadsaveurs.searcher.models import MissionReclamation


class MissionReclamationSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = MissionReclamation
        fields = ("id", "user", "description")


class MissionReclamationSerializerIn(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MissionReclamation
        fields = ("id", "user", "description")
