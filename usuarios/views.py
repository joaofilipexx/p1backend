from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Usuario
import json

def lista_usuarios(request):
    """Lista todos os usuários ou filtra por status ativo"""
    usuarios = Usuario.objects.all()
    
    data = {
        'usuarios': [
            {
                'id': u.id,
                'nome': u.nome,
                'email': u.email,
                'ativo': u.ativo,
                'data_criacao': u.data_criacao.isoformat()
            }
            for u in usuarios
        ]
    }
    return JsonResponse(data)

def detalhe_usuario(request, id):
    """Retorna os detalhes de um usuário específico"""
    usuario = get_object_or_404(Usuario, id=id)
    
    data = {
        'id': usuario.id,
        'nome': usuario.nome,
        'email': usuario.email,
        'ativo': usuario.ativo,
        'data_criacao': usuario.data_criacao.isoformat()
    }
    return JsonResponse(data)