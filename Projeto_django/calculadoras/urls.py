from django.urls import path
from . import views

urlpatterns = [
    path('calculadoras/calc-sal-liquido', views.calc_sal_liq, name='calc-sal-liquido'),
    path('calculadoras/calc-imp-renda', views.calc_imp_renda, name='calc-imp-renda'),
    path('calculadoras/calc-ferias', views.calc_ferias, name='calc-ferias'),
]