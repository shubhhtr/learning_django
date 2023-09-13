from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h2>Welcome</h2><a href='/recipes'>Go to Recipe App</a>")

def contacts(request):

    data = [
        {'name':'Test', 'age':23, 'gender': 'male'},
        {'name':'qwerty', 'age':33, 'gender': 'male'},
        {'name':'pooja', 'age':20, 'gender': 'female'},
    ]

    return render(request, "contact.html", context= {'data': data})
