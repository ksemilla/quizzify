from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from quizzify.core.middleware import get_current_user
from quizzify.core.models import (
    BigForeignKey,
    BaseModel
)

class User(AbstractUser):
    """Default user for Quizzify."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    main_team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True)

class StampedModel(BaseModel):
    created_by = BigForeignKey(User,
        related_name='%(class)s_created_by',
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    modified_by = BigForeignKey(User,
        related_name='%(class)s_modified_by',
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user:
            self.modified_by = user
            if not self.id:
                self.created_by = user
        super(StampedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class Team(StampedModel):

    name = models.CharField(max_length=128)

class Member(StampedModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)