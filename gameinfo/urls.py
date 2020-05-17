from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = (
       url(r'^$', login_required(views.gameinfoList.as_view()), name="game_info"),
       url(r'^view_post/(?P<pk>\d+)/(?P<is_file>\d+)/$', views.view_post, name='view_post'),
       url(r'^create/$', views.create, name='create_gameinfo'),
       url(r'^(?P<pk>\d+)/update/$', views.update, name='update_gameinfo'),
       url(r'^(?P<pk>\d+)/delete/$',  views.delete,  name='delete_gameinfo'),
       url(r'^movie/(?P<pk>\d+)/delete/$',  views.delete_movie,  name='delete_movie'),
       url(r'^subtitle/(?P<pk>\d+)/delete/$', views.delete_subtitle, name='delete_subtitle'),
       url(r'^moviedetail/(?P<pk>\d+)/delete/$', views.delete_moviedetail, name='delete_moviedetail'),
       url(r'^setting/(?P<pk>\d+)/delete/$', views.delete_setting, name='delete_setting'),
       url(r'^faq/(?P<pk>\d+)/delete/$', views.delete_faq, name='delete_faq'),
       url(r'^desc/(?P<pk>\d+)/delete/$', views.delete_desc, name='delete_desc'),
       url(r'^image/(?P<pk>\d+)/delete/$', views.delete_image, name='delete_image'),
       url(r'^subimage/(?P<pk>\d+)/delete/$', views.delete_subimage, name='delete_subimage'),
       url(r'^summary/(?P<pk>\d+)/delete/$', views.delete_summary, name='delete_summary'),
       url(r'^filters/(?P<pk>\d+)/(?P<page>\d+)$', views.filters, name='view_filters'),
       url(r'^filters_v2/(?P<pk>\d+)$', views.view_fillters_v2, name='view_filters_v2'),
       url(r'^thema/(?P<pk>\d+)/(?P<page>\d+)$', views.thema, name='view_thema'),
       url(r'^vod/(?P<pk>\d+)$', views.view_vod, name='view_vod'),
       url(r'^movies-thumbnail/(?P<pk>\d+)/(?P<movies_id>\d+)$', views.view_movies_thumbnail, name='view_movies_thumbnail'),
       url(r'^gameinfo-autocomplete/$',  views.GameInfoAutocomplete.as_view(), name='gameinfo-autocomplete',),
)