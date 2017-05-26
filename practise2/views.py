from time import timezone
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import DetailView,UpdateView,DeleteView,CreateView,FormView, View
from practise2.models import MyModel
from django.urls import reverse_lazy
from practise2.forms import ContactForm,CreateForm
from django.views.generic import TemplateView
# Create your views here.

class CreateModel(CreateView):


    #fields = ("name","age")
    template_name = "practise2/create.html"
    model = MyModel
    form_class = CreateForm
    success_url = reverse_lazy("home")

class GenericContactForm(FormView):
    #success_url = reverse_lazy("home")
    template_name = "practise2/contact.html"
    form_class = ContactForm
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        #return super(GenericContactForm, self).form_valid(form)
        return HttpResponseRedirect(reverse_lazy("home"))



class ArticleDetailView(DetailView):
    model = MyModel
    template_name = "practise2/article-detail.html"
    #not mandatory i guess it has to do with the base class
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context["place"]={"city":"mexico city","country":"mexico","continent":"America"}


        return context



class UpdateModel(UpdateView):
    model = MyModel
    fields = ('name',"age")

    template_name = "practise2/update.html"
    success_url = reverse_lazy("home")




class DeleteModal(DeleteView):
    model = MyModel
    success_url = reverse_lazy("home") #"/prac2/class"
    template_name = "practise2/modal_check_delete.html"  #template_name should be suffixed with check_delete.html b




class Class_Based_View(View):
    template_name="practise2/create.html"
    def get(self, request, *args, **kwargs):


        return render(request,template_name=self.template_name,context={"form":CreateForm(request.GET)})
    def post(self,request):
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse_lazy("home"))
        return render(request,template_name=self.template_name,context={"form":CreateForm(request.GET)})


#this is the default way it used to be done before the introduction generic views
def default_detailed_selection(request,selection):
    print("this is the selection",selection)
    return HttpResponse("hello world")