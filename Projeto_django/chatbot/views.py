from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone


openai_api_key = ''
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are an expert in finance and accounting. It should act as a virtual assistant for my 'free financial education' website. Help users with case-specific mentoring and guidance. Any talk other than finance should be rejected. Start with a message - Olá, sou seu assistente virtual de finanças. Faça uma pergunta! "},
            {"role": "user", "content": message},
    ],
    )
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})

def logout(request):
    auth.logout(request)
    return redirect('home')
