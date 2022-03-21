from django.shortcuts import get_object_or_404, render
from .models import Receita

def index(request):
    dados = {
        'receitas': Receita.objects.all()
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):

    receita_a_exibir = {
        'receita': get_object_or_404(Receita, pk=receita_id)
    }

    return render(request, 'receita.html', receita_a_exibir)