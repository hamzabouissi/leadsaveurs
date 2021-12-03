from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime

# Create your models here.
from leadsaveurs.users.models import UserSaved, Saver


class MissionsStatusEnum(models.TextChoices):
    Pending = "Pending", _("Pending")
    Accepted = "Accepted", _("Accepted")
    Rejected = "Rejected", _("Rejected")


class Boat(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    max_size = models.PositiveIntegerField(default=1)


class Mission(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    saved_users = models.ManyToManyField(UserSaved, related_name="missions")
    savers = models.ManyToManyField(Saver, related_name="landed_missions")
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, related_name="missions")
    captain = models.ForeignKey(Saver, on_delete=models.CASCADE, related_name="missions")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    start_location = models.CharField(max_length=25, blank=False, null=False)
    end_location = models.CharField(max_length=25, blank=False, null=False)
    status = models.CharField(MissionsStatusEnum.choices, max_length=25, default=MissionsStatusEnum.Pending)

    @property
    def duration(self):
        return self.end_date - self.start_date

    @property
    def is_missing(self):
        return datetime.today() - self.end_date


class TechnicalReclamation(models.Model):
    user = models.ForeignKey(Saver, on_delete=models.CASCADE)
    description = models.TextField(max_length=250)


class MissionReclamation(models.Model):
    user = models.ForeignKey(Saver, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    description = models.TextField(max_length=250)


class Donation(models.Model):
    user_saved = models.ForeignKey(UserSaved, on_delete=models.CASCADE)
