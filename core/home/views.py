from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h2>Testing</h2>")

def contacts(request):
    return render(request, "contact.html")
