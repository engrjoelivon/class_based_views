from django.db import models

# Create your models here.
class Task(models.Model):
    task_id=models.IntegerField(null=False,blank=False)
    task_name=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.task_name
    class Meta:
       verbose_name="Record name"

