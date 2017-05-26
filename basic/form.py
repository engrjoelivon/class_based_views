from django import forms
from basic.models import Task
class MyTask(forms.ModelForm):
    task_id=forms.IntegerField(help_text="enter the id")
    task_name=forms.CharField(help_text="enter your name",max_length=200)
    class Meta:
        model=Task
        fields = ("task_name" ,"task_name")
