from django.conf.urls import url
from django.views.generic import TemplateView,ListView,DetailView
from practise2.models import MyModel
from practise2.views import ArticleDetailView,default_detailed_selection,UpdateModel,DeleteModal,CreateModel,GenericContactForm,Class_Based_View




urlpatterns=[

    url("^$", ListView.as_view(template_name="practise2/home.html", model=MyModel), name="home"),
    url(r"^cbv/$",Class_Based_View.as_view(),name="cbv"),
    url("^create/$", CreateModel.as_view(), name="create"),
    url("^contact/$", GenericContactForm.as_view(), name="contact"),
             #url(r'^(?P<pk>[-\w]+)/$', DetailView.as_view(queryset=MyModel), name='article-detail'),
    url(r'^(?P<pk>[-\w]+)/delete$', DeleteModal.as_view(), name='modal-delete'),
    url(r'^(?P<pk>[-\w]+)/$', ArticleDetailView.as_view(), name='modal-detail'),

    url(r'^(?P<pk>[-\w]+)/update$',UpdateModel.as_view(), name='modal-update'),

             #url(r'^(?P<selection>[-\w]+)/$', view=default_detailed_selection, name='article-detail'),

    #UpdateModel.as_view(), name='article-detail'),
             ]