from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models

class UserRoleEnum(models.TextChoices):
    Saver = "Saver", _("Saver")
    UserSaved = "Inst", _("User Saved")
    NormalUser = "NUser", _("Normal User")


class User(AbstractUser):
    """Default user for LeadSaveurs."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    role = models.CharField(choices=UserRoleEnum.choices,max_length=25,null=False,blank=False,default=UserRoleEnum.NormalUser)
    location = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True,blank=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})



class Saver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    grade = models.CharField(max_length=25, blank=False,null=False,default="A")



    @property
    def missions_count(self)-> int:
        return self.landed_missions.count()

    @property
    def people_saved_count(self):
        return self.landed_missions.values_list("saved_users").count()


class UserSaved(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_alive = models.BooleanField(default=True)

    @property
    def missions_count(self) -> int:
        return self.missions.count()

