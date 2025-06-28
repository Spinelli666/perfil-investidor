from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def home(request):
    """View para a página inicial"""
    return render(request, 'questionario/home.html')

def questionario(request):
    """View para o questionário de perfil de investidor"""
    if request.method == 'POST':
        # Aqui será processado o questionário quando as perguntas forem adicionadas
        messages.success(request, 'Questionário submetido com sucesso!')
        return redirect('questionario:resultado')
    
    return render(request, 'questionario/questionario.html')

def resultado(request):
    """View para exibir o resultado do perfil de investidor"""
    # Por enquanto, um resultado mock - será implementado conforme as perguntas
    perfil = "Conservador"  # Isso será calculado baseado nas respostas
    return render(request, 'questionario/resultado.html', {'perfil': perfil})
