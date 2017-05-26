from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, RedirectView,View
from basic.models import Task
from django.http import HttpResponse, HttpResponseRedirect
from basic.form import MyTask
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required





class BasicClassAsView(View):
    """
       #does not work by defining only template name,must specify get
       return works

    """
    def get(self,request):
      return render(request,"basic/home.html",{"mylist":Task.objects.all()})



class BasicClassAsViewUsingTemplateView(TemplateView):

       template_name = "basic/home.html" #works by defining just template_name
      # model="Task"  does not work



       def get(self,request): #using only this get als works   #works
           return render(request,"basic/home.html",
                         {"object_list":Task.objects.all()}
                         )


def functionBasedVied(request):
           print("in functionBasedVied")
           ones=Task.objects.all()
           context_dict={"ones":ones}
           return render(request,"task.html",{"object_list":Task.objects.all()}
                         #{"ones":Task.objects.all()}
                         )



class MyView(TemplateView):
    greeting=""

    def get(self, request):
        # <view logic>
        return render(request,"task.html",{"form":MyTask()} )

    def post(self ,request):
        form=MyTask(request.POST)
        if  form.is_valid():
            print("it is valid")
            return HttpResponse("done")
        else:
            messages.error(request, "Error")
        return render(request,"task.html",{"form":MyTask()} )








@method_decorator(login_required, name="dispatch")
class ProtectedView(TemplateView):
      template_name="admin.html"

      def dispatch(self, request, *args, **kwargs):
          return super().dispatch(request, *args, **kwargs)

