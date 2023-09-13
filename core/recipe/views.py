from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.

@login_required(login_url='/login')
def recipes(request):
    if(request.method == 'POST'):
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipes.objects.create(recipe_name = recipe_name, recipe_description = recipe_description, recipe_image = recipe_image)
        return redirect('/recipes/')
    
    queryset = Recipes.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    
    context = {'recipes': queryset}
    return render(request, 'recipes.html', context= context)


@login_required(login_url='/login')
def delete_recipe(request, id):
    queryset = Recipes.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes')

@login_required(login_url='/login')
def update_recipe(request, id):
    queryset = Recipes.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_description = recipe_description
        queryset.recipe_name = recipe_name

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes/')
        
    
    return render(request, 'update_recipe.html', context={'recipe': queryset})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid username")
            return redirect('/login')

        user = authenticate(username = username, password= password)
        if user is None:
            messages.error(request, 'Invalid Password')
            redirect('/login')
        else:
            login(request, user=user)
            return redirect('/recipes') 

    return render(request, "login.html")

def signup_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.add_message(request, messages.INFO, "Username already taken!")
            return redirect('/signup')

        user= User.objects.create(first_name= first_name, last_name= last_name, username=username)
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully")
        return redirect('/signup')

    return render(request, "signup.html")

def logout_page(request):
    logout(request)
    return redirect('/login')
