from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =  [
    #url('^$', views.HomePageView.as_view()),
    #url('^$', views.IndexPageView.as_view()),
    path('', views.home, name='index'),
    url('^about/$', views.AboutPageView.as_view()),
]