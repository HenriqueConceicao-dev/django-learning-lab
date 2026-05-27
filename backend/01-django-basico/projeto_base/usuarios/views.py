from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse('login usuario')

def cliente(request):
    return render(request, 'cliente.html')