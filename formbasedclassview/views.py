from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View


class MyFormView(View):
    initial = {'key': 'value'}
    template_name = 'form_template.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,"task.html",{"form":form} )


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request,"task.html",{"form":form} )
