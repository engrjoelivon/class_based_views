from django import forms
from django.db import models
from practise2.models import MyModel


class ContactForm(forms.Form):
    name=forms.CharField(max_length=50,help_text="enter your inputs here")
    age = forms.IntegerField()


    def send_email(self):
        pass

    class Meta:
        models=MyModel
        fields=("name","age")




class CreateForm(forms.ModelForm) :
    class Meta:
        model=MyModel
        fields=("name","age")


    def save(self, commit=True):
        user=super().save(commit=False)
        user.save()
        return user