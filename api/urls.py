from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from django.contrib.auth.decorators import login_required

from .api import *
from .views import *

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = (
#    url(r'^doc/', login_required(schema_view), name="docs"),
    url(r'^signup/$', SignUp.as_view(), name="sign_up"),
    url(r'^current-user/', CurrentUserView.as_view()),
    url(r'^login/', login),
    url(r'^guide-movie/(?P<branch>[0-9]+)/$', guide_movie),
    url(r'^course/(?P<branch>[0-9]+)/$', course_list),
    url(r'^layer/(?P<branch>[0-9]+)/$', layer),
    url(r'^layer-sub/(?P<layer>[0-9]+)/$', layer_sub),
    url(r'^etc/$', etc),
    url(r'^movies/$', MoviesList.as_view(), name='movies-list'),
    url(r'^game-thema/$', gameThema_list),
    url(r'^gamelist-all/$', gameinfoAll_list),
    url(r'^gamelist/(?P<branch>[0-9]+)/$', branchGameinfo_list),
    url(r'^gamelist_v2/(?P<branch>[0-9]+)/$', branchGameinfo_list_v3),
    url(r'^gamelist_v3/(?P<branch>[0-9]+)/$', branchGameinfo_list_v3),
    url(r'^email/$', sendEmail),
    url(r'^togeter-joinlist/$', togetherJoinList_add),
    url(r'^togeter-joinlist/(?P<branch_id>[0-9]+)/$', togetherJoinList_list),
    url(r'^togeter-joinlist/(?P<branch_id>[0-9]+)/delete-branch/$', togetherJoinList_delete_branch),
    url(r'^togeter-joinlist/(?P<branch_id>[0-9]+)/(?P<room_id>[0-9]+)/delete-room/$', togetherJoinList_delete_room),
    url(r'^togeter-join/$', togetherJoin_add),
    url(r'^togeter-join/(?P<branch_id>[0-9]+)/(?P<room_id>[0-9]+)/$', togetherJoin_list),
    url(r'^togeter-join/delete/$', togetherJoin_list_delete),
    url(r'^togeter-join-accept/$', togetherJoin_accept_add),
    url(r'^togeter-join-accept/(?P<branch_id>[0-9]+)/(?P<room_id>[0-9]+)/$', togetherJoin_accept_list),
    url(r'^togeter-join-accept/delete/$', togetherJoin_accept_list_delete),
    url(r'^togeter-message/$', togeterMessage_add),
    url(r'^togeter-message/(?P<branch_id>[0-9]+)/(?P<room_id>[0-9]+)/$', togeterMessage_list),
    url(r'^togeter-message/delete/$', togeterMessage_list_delete),
    url(r'^firebase/$', firebase_add),
    url(r'^firebase/(?P<branch_id>[0-9]+)/(?P<room_id>[0-9]+)/$', firebase_get),

)
