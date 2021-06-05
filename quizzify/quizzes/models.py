from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from quizzify.users.models import (
    StampedModel,
    User,
)

class Quiz(StampedModel):

    class Types(models.TextChoices):
        DEFAULT         = 'default', _('Default')
        LIMITED         = 'limited', _('Limited')

    # team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=256)

    type = models.CharField(max_length=16, choices=Types.choices, default=Types.DEFAULT)

    opens_on = models.DateTimeField(default=timezone.now)
    closes_on = models.DateTimeField(default=timezone.now)

class QuizItem(StampedModel):

    class Types(models.TextChoices):
        SINGLE          = 'default', _('Default')
        MULTI           = 'limited', _('Limited')
        TEXT            = 'text', _('text')

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    order = models.IntegerField()
    question = models.CharField(max_length=256)
    answer = models.TextField(max_length=10000)
    photo = models.ImageField(null=True)
    weight = models.IntegerField(default=1)

class ItemChoice(StampedModel):
    quiz_item = models.ForeignKey(QuizItem, on_delete=models.CASCADE)
    order = models.IntegerField()
    text = models.CharField(max_length=128)

class Answer(StampedModel):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class QuizItemAnswer(StampedModel):
    quiz_item = models.ForeignKey(QuizItem, on_delete=models.CASCADE)
    answer = models.TextField(max_length=10000)
