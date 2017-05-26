from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView,View,DetailView
from django.views.generic.list import ListView
from basic.views import MyView,ProtectedView

from basic import urls as basicurl
from formbasedclassview import urls as formurls
from generic_views import urls as genericurl
from generic_views.views import PublisherList,PublisherDetail,AuthorForm
from generic_views.models import Publisher,Book,Author
from practise2 import urls as practiseurl


urlpatterns = [
    # Examples:
    url(r'^$', TemplateView.as_view( template_name="index.html"),name="index"),
    url(r'^owner/$', TemplateView.as_view(template_name="admin.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', MyView.as_view(greeting="G'day"),name="about"),  #added the about tag.
    url(r'^pro/$', ProtectedView.as_view()),

    url(r'^login/$', TemplateView.as_view(template_name="login.html")),
    url(r'^basic/',include(basicurl)),
    url(r'^listview/',include(genericurl)),
    url(r'^formview/',include(formurls)),
    url(r'^prac2/',include(practiseurl))






]
