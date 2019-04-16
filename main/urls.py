from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = (
       url(r'^$', login_required(views.index), name="main_index"),
       url(r'^(?P<branch_id>\d+)/(?P<is_file>\d+)/(?P<layer_div>\d+)/create/$', views.create, name="create_main"),
       url(r'^guide/(?P<branch_id>\d+)/(?P<pk>\d+)/delete/$',  views.delete_guide,  name='delete_guide'),
       url(r'^course/(?P<branch_id>\d+)/(?P<pk>\d+)/delete/$', views.delete_course, name='delete_course'),
       url(r'^layer/(?P<branch_id>\d+)/(?P<pk>\d+)/delete/$', views.delete_layer, name='delete_layer'),
       url(r'^layersub/(?P<branch_id>\d+)/(?P<layer_id>\d+)/(?P<layer_div>\d+)/create/$', views.layersub_create, name='create_layersub'),
       url(r'^layersub/(?P<branch_id>\d+)/(?P<layer_id>\d+)/(?P<layer_div>\d+)/(?P<pk>\d+)/delete/$', views.delete_layersub, name='delete_layersub'),

)