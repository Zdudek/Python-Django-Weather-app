#WEATHER URLS.PY
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list_all', views.list_all, name  ="list_all"),
    url(r'^add', views.add, name  ="add"),
    url(r'^about', views.about, name  ="about"),
    url(r'^forecast', views.forecast, name  ="forecast"),
    url(r'^manchester', views.manchester, name  ="manchester"),
    url(r'^boston', views.boston, name  ="boston"),
    url(r'^nyc', views.nyc, name  ="nyc"),
    url(r'^temp', views.templete, name  ='temp'),	
    url(r'^home/', views.home, name  ="home"),    
]