from django.urls import path
from . import views

urlpatterns = [
    path('investimentos/tesouro-direto', views.tesouro_direto, name='tesouro-direto'),
    path('investimentos/inv-longo-prazo', views.inv_longo_prazo, name='inv-longo'),
    path('investimentos/inv-curto-prazo', views.inv_curto_prazo, name='inv-curto'),
    path('logout', views.logout, name='logout'),
]