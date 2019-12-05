from django.conf.urls import url
from . import views
#this url is connected to page one local host 8000                   
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.process_money)
]