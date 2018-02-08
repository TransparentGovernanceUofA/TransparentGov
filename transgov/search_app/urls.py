from django.conf.urls import url
from search_app import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

]
