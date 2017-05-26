from generic_views.models import Author
from django import forms



class AuthorForm(forms.Form):
    salutation=forms.CharField(max_length=10)
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    headshot=forms.ImageField()
    def sendemail(self):
        pass
    class Meta:
        model=Author
        fields = ("name" ,"salutation","email","headshot")


