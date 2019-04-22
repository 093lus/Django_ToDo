from django.conf.urls import url
from task import views

urlpatterns = [
    url(r'^$', views.TaskList.as_view(), name='list'),
    url(r'^create/$', views.TaskCreate.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)/$', views.TaskDelete.as_view(), name='delete'),
    url(r'^search/(?P<key>[^/]+)/$', views.TaskSearch.as_view(), name='search'),
    url(r'^reorder/$', views.TaskReorder.as_view(), name='reorder'),
           ]