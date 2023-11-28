from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)  # NOTA: Isso não é a melhor prática, use algo como Django's built-in User model ou hash senhas adequadamente.