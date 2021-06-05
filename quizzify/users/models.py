from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from quizzify.core.middleware import get_current_user
from quizzify.core.models import (
    BigForeignKey,
    BaseModel
)

from .const import UserScopes

class User(AbstractUser):
    class ScopeChoices(TextChoices):
        ADMIN       = 'admin', _('Admin')
        USER        = 'user', _('User')
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(max_length=128)
    last_name = CharField(max_length=128)
    main_team_id = models.BigIntegerField(null=True)

    scope = models.CharField(max_length=32, choices=ScopeChoices.choices, default=UserScopes.USER)
    is_frozen = models.BooleanField(default=False)

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
