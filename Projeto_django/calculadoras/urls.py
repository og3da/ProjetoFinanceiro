from django.urls import path
from . import views

urlpatterns = [
    path('calculadoras/calc-sal-liquido', views.calc_sal_liq, name='calc-sal-liquido'),
]