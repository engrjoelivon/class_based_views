from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from generic_views.models import Publisher, Book
from django.views.generic.edit import FormView
from generic_views.forms import AuthorForm


class PublisherList(ListView):

    #model = Publisher
    #template_name = "generic_views/publisher_list.html"
    #context_object_name = 'my_favorite_publishers'
    #paginate_by = 5
    #queryset = Publisher.objects.all()


    def get(self, request):
        return render(request,"generic_views/publisher_list.html",{"my_favorite_publishers":Publisher.objects.all()})
    def post(self):

        return HttpResponse()


class PublisherDetail(DetailView):
    context_object_name = "task"

    template_name = "generic_views/publisher_detail.html"
    model = Publisher
    queryset = Publisher.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context["books_list"] = Book.objects.all()
        return context


class AuthorForm(FormView):
    template_name = "generic_views/contact.html"
    form_class = AuthorForm
    success_url = "/success/"

    def form_valid(self, form):
        print("its valid")
        return super(AuthorForm, self).form_valid(form)
