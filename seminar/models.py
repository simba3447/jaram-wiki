from django.db import models
from django.contrib.auth.models import User
from main.models import TimeStampedModel

# Create your models here.
class BasePostModel(TimeStampedModel):
    writer = models.ForeignKey(User)

    class Meta:
        abstract = True
