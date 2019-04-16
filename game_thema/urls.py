from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = (
       url(r'^$', login_required(views.list), name="game_thema"),
       url(r'^create/$', views.create, name='create_game_thema'),
       url(r'^(?P<pk>\d+)/update/$', views.update, name='update_game_thema'),
       url(r'^(?P<pk>\d+)/delete/$', views.delete, name='delete_game_thema'),
     #     url(r'^$', login_required(views.gamethema_settings), name="game_thema"),

)