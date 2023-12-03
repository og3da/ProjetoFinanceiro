from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
def tesouro_direto(request):
    return render(request, 'tesouro-direto.html')

def inv_longo_prazo(request):
    return render(request, 'inv-longo.html')

def inv_curto_prazo(request):
    return render(request, 'inv-curto.html')

def logout(request):
    auth.logout(request)
    return redirect('login')