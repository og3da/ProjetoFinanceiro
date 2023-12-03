from django.contrib import auth
from django.shortcuts import render, redirect


def aprenda_economizar(request):
    return render(request, 'plan-eco.html')

def negociar_dividas(request):
    return render(request, 'plan-div.html')

def logout(request):
    auth.logout(request)
    return redirect('home')