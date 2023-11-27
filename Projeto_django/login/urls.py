from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
]
