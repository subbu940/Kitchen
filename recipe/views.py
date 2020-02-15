from django.shortcuts import render
from .models import Recipe
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'recipe/index.html', {'recipe_list':recipe_list})


def details(request):
    Recipe.objects.create(name=request.POST['name'],
                          ingredients=request.POST['ingredients'],
                          process=request.POST['process']
                          )
    return HttpResponseRedirect(reverse('recipe:index'))
    return render(request, 'recipe/create.html')


def save(request):
    Recipe.objects.create(name= request.POST['name'],
                          ingredients=request.POST['ingredients'],
                          process=request.POST['process']
                         )
    return HttpResponseRedirect(reverse('recipe:index'))


def display(request, res_id):
    recipe = Recipe.objects.get(pk=res_id)
    return render(request, 'recipe/display.html', {'recipe': recipe})

