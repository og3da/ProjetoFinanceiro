from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#import logging

#logger = logging.getLogger(__name__)


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

@csrf_exempt
def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        print()
        print("----- LOGS")
        if not nome or not email or not senha:
            # Retorna uma resposta indicando que o cadastro falhou
            print("Todos os campos são obrigatórios. Preencha todos os campos.")
            mensagem = "Todos os campos são obrigatórios. Preencha todos os campos."
            return render(request, 'login.html', {'mensagem': mensagem})

        # Verifique se o email já está em uso
        if Usuario.objects.filter(email=email).exists():
            print("O email já está em uso. Escolha outro email!")
            mensagem = "O email já está em uso. Escolha outro email!"
            return render(request, 'login.html', {'mensagem': mensagem})

        # Cria um novo objeto Usuario e o salva no banco de dados
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()

        # Retorna uma resposta indicando que o cadastro foi bem-sucedido
        print("Usuario Cadastrado")
        mensagem = "Operação realizada com sucesso!"
        return render(request, 'login.html', {'mensagem': mensagem})

    # Retorna uma resposta indicando que a requisição não é válida (não é um POST)
    mensagem = "Método de requisição não permitido.!"
    return render(request, 'login.html', {'mensagem': mensagem})

@csrf_exempt
def login_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        print()
        print("----- LOGS")
        if not email or not senha:
            # Retorna uma resposta indicando que o cadastro falhou
            print("Todos os campos são obrigatórios. Preencha todos os campos.")
            mensagem = "Todos os campos são obrigatórios. Preencha todos os campos."
            return render(request, 'login.html', {'mensagem': mensagem})

        # Verifique se o email já está em uso
        if not Usuario.objects.filter(email=email).exists():
            print("O email não existe, cadastre-se!")
            mensagem = "O email não existe, cadastre-se!"
            return render(request, 'login.html', {'mensagem': mensagem})

        # Verifique se a senha já está em uso
        if not Usuario.objects.filter(senha=senha).exists():
            print("Senha incorreta!")
            mensagem = "Senha incorreta!"
            return render(request, 'login.html', {'mensagem': mensagem})
        
        print("Login Realizado!")
        mensagem = "Login Realizado!"
        return render(request, 'home.html', {'mensagem': mensagem})

    # Retorna uma resposta indicando que a requisição não é válida (não é um POST)
    mensagem = "Método de requisição não permitido.!"
    return render(request, 'login.html', {'mensagem': mensagem})