from django.conf.urls import include, url
from generic_views.views import PublisherList,PublisherDetail,AuthorForm




urlpatterns = [url(r'^$',PublisherList.as_view(),name="listview"),
               url(r'^(?P<pk>\d+)/$',PublisherDetail.as_view()),
                url(r'^addauthor/$',AuthorForm.as_view(),name="author"),

               ]