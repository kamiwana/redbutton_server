from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = (
       url(r'^$', login_required(views.create), name="create_etc"),
)