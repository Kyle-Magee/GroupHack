from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.add_user),
    url(r'^language', views.choose_language),
    url(r'^interests', views.interest),
    url(r'^users', views.show_users),
]