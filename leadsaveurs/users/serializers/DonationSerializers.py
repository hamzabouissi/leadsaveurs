from rest_framework import serializers

from leadsaveurs.searcher.models import Donation
from leadsaveurs.users.models import User


class DonationMicroUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email", "location", "phone")


class DonationSerializerOut(serializers.ModelSerializer):
    user_saved = DonationMicroUserSerializer()

    class Meta:
        model = Donation
        fields = ("id", "user_saved")


class DonationSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ("id", "user_saved")
