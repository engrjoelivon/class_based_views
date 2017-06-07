from django.conf.urls import url
from django.views.generic import TemplateView
from url_exe import views


urlpatterns = [ url(r"^/$",TemplateView.as_view(template_name="url_exe\home.html")),

                url(r'^(?P<slug>[-\w]+)/$',views.MyDetailView.as_view()),
                url(r'^(?P<slug>[-\w]+)')
                ]
