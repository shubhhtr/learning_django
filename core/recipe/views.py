from django.shortcuts import render

# Create your views here.

def recipes(request):
    data = request.POST
    print(data)
    return render(request, 'recipes.html')
