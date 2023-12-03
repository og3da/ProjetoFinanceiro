from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
def calc_sal_liq(request):
    return render(request, 'calc-sal-liquido.html')

def calc_imp_renda(request):
    return render(request, 'calc-imp-renda.html')

def calc_ferias(request):
    return render(request, 'calc-ferias.html')

def logout(request):
    auth.logout(request)
    return redirect('login')