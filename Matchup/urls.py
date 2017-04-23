from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page),
    url(r'^language', views.choose_language),
    url(r'^interests', views.interest),
]