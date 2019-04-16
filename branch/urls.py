from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = (
       url(r'^$', login_required(views.branchList.as_view()), name="list_branch"),
       url(r'^create/$', views.create, name='create_branch'),
       url(r'^(?P<pk>\d+)/update/$', views.update, name='update_branch'),
       url(r'^(?P<pk>\d+)/delete/$', views.delete, name='delete_branch'),
)