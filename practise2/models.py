from django.db import models
from datetime import datetime
import pytz
from pytz import UTC
from django.utils import timezone
# Create your models here.
class MyModel(models.Model):

    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    age=models.PositiveSmallIntegerField(default=0)
    time=models.DateTimeField(default=datetime.now(tz=UTC),null=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering=["name",]
