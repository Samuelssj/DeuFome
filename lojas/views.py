from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Loja

# Create your views here


def index(request):

    lojas = Loja.objects.all()

    dados = {
        'lojas': lojas
    }

    return render(request, 'index.html', dados)


def loja(request, loja_id):

    loja = get_object_or_404(Loja, pk=loja_id)

    loja_a_exibir = {
        'loja': loja
    }

    return render(request, 'index.html', loja_a_exibir)
