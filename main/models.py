from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(_('작성일'), auto_now_add=True)
    modified = models.DateTimeField(_('수정일'), auto_now=True)

    class Meta:
        abstract: True
