from django.shortcuts import render
from django.views.generic import DetailView
from url_exe import models
# Create your views here.
class MyDetailView(DetailView):
    template_name ="url_exe/infodetail.html"
    model = models.Task
