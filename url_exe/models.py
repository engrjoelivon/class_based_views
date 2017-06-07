from django.db import models

# Create your models here.
from django.urls import reverse


class Task(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    age=models.PositiveSmallIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __unicode(self):
        return self.name