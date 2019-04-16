from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = (
       url(r'^$', login_required(views.memberList.as_view()), name="member_list"),
       url(r'^create/$', views.create, name='create_member'),
       url(r'^(?P<id>\d+)/update/$', views.update, name='update_member'),
       url(r'^(?P<id>\d+)/delete/$', views.delete, name='delete_member'),
       url(r'^(?P<id>\d+)/password/$', views.password_reset, name='password_reset_member'),
)