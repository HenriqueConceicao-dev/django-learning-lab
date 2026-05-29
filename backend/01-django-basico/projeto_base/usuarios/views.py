from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente

def cadastro(request):
    return HttpResponse('login usuario')

def cliente(request):
    if request.method == 'GET':
        return render(request, 'cliente.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        queixa = request.POST.get('queixa')

        if len(nome) <= 2 :
            return redirect('cliente')
        
        cliente = Cliente(nome=nome, email=email, queixa=queixa)

        cliente.save()

        return redirect('cliente')


    