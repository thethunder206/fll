from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('abs.html', views.abs, name="abs"),
    path('pho.html', views.pho, name="pho"),
    path('whi.html', views.whi, name="whi"),
]