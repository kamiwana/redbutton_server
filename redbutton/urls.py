"""redbutton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    url(r'^rest-swagger/', include('rest_framework_swagger.urls')),
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from member import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #   url(r'^', include(router.urls)),
    # 인증처리를 위한 url
    url(r'^$', login_required(views.memberList.as_view()), name="member_list"),
    url(r'^branch/', include('branch.urls')),
    url(r'^branch_game/', include('branch_gameinfo.urls')),
    url(r'^gameinfo/', include('gameinfo.urls')),
    url(r'^member/', include('member.urls')),
    url(r'^main/', include('main.urls')),
    url(r'^etc/', include('etc.urls')),
    url(r'^together/', include('togeter.urls')),
    url(r'^game_thema/', include('game_thema.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('api.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
