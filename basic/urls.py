from django.conf.urls import url
from django.views.generic import TemplateView, View
from basic.views import BasicClassAsView,BasicClassAsViewUsingTemplateView,functionBasedVied
urlpatterns=[
   #url(r'^$', TemplateView.as_view(template_name="basic/home.html"), name="basic"), #correct #can not pass model here
      #url(r'^$', BasicClassAsView.as_view(), name="basic"),    #does not work
         #url(r'^$',View.as_view(template_name="basic/home.html"), name="basic"),    #does not work

   url(r'^$', BasicClassAsViewUsingTemplateView.as_view(), name="basic") #correct
   #url(r'^$',functionBasedVied,name="basic")

]
