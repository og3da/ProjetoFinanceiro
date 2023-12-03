from django.http import HttpResponse
from django.template import loader
from django.contrib import auth
from django.shortcuts import render, redirect

def main(request):
    return render(request, 'principal.html')

def home(request):
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return redirect('login')