from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
]