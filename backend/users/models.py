from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.
    """
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    group = models.ManyToManyField(
        "course.Group",
        blank=True,
        related_name="user_group",
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
