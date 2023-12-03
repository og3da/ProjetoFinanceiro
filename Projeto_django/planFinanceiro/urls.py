from django.urls import path
from . import views

urlpatterns = [
    path('planFinanceiro/aprenda-economizar', views.aprenda_economizar, name='aprenda-economizar'),
    path('planFinanceiro/negociar-dividas', views.negociar_dividas, name='negociar-dividas'),
    path('logout', views.logout, name='logout'),
]
