from django.db import models
from model_utils.models import TimeStampedModel

from quizzify.core.helpers import generate_random_id

class BaseModel(TimeStampedModel):
    id = models.BigIntegerField(default=generate_random_id, primary_key=True)

    class Meta:
        abstract = True

class BigForeignKey(models.ForeignKey):
    def db_type(self, connection):
        return 'BIGINT'

    def rel_db_type(self, connection):
        return 'BIGINT'

