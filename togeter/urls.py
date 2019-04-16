from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = (
       url(r'^$', login_required(views.index), name="togetherMessageLog_index"),
       url(r'^(?P<branch_id>\d+)/togetherMessageLog-list/$', views.togetherMessageLogList.as_view(), name="togetherMessageLog_list"),
)