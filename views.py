from django.shortcuts import render
from django.http import HttpResponse

posts = ['Новые тренды в моде', 'Лучшие места для отпуска', 'Интересные факты о животных']

def index(request):
    data = {
        'name': 'Александр',
        'last_name': 'Белов',
        'email': 'belov@jmail.com',
        'birthday': '12.09.1994',
        'posts': posts
    }
    return render (request, 'index.html', context=data)

def contacts(request):
    return render (request, 'contact.html' )




