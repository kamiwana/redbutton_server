from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = (
       url(r'^$', login_required(views.index), name="branchgame_index"),
       url(r'^(?P<branch_id>\d+)/branchgame-list/$', views.branchgameList.as_view(), name="branchgame_list"),
       url(r'^(?P<branch_id>\d+)/insert/$',views.branchgame_insert,name='branchgame_insert'),
       url(r'^(?P<branch_id>\d+)/branchgame-all-insert/$',views.branchgame_all_insert, name='branchgame_all_insert'),
)