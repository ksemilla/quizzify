from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from quizzify.users.models import (
    StampedModel,
    User,
)

class Organization(StampedModel):
    name = models.CharField(max_length=128)

class Member(StampedModel):
    team = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    