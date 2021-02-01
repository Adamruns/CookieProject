from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Recipe
from . import models


class IndexView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        context = {
            'recipes': recipes,
            'title': 'Cookies',
        }
        return render(request, 'recipes/index.html', context)


class RecipeListView(View):
    pass


class RecipeAddView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'recipes/recipe_form.html', context)

    def post(self, request):
        title = self.request.POST.get('title')
        yield_amount = self.request.POST.get('yield_amount')
        prep_time = self.request.POST.get('prep_time')
        ingredients = self.request.POST.get('ingredients')
        directions = self.request.POST.get('directions')
        image = self.request.POST.get('image')

        recipe = models.Recipe.objects.create(title=title, yield_amount=yield_amount, prep_time=prep_time,
                                              ingredients=ingredients, directions=directions, image=image)
        return HttpResponseRedirect(reverse('recipe_index'))


class RecipeEditView(View):
    def get(self, request, pk=None):
        recipe = Recipe.objects.get(pk=pk)
        return render(request, 'recipes/recipe_edit.html', context={'recipe': recipe})

    def post(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        recipe.title = self.request.POST.get('title')
        recipe.yield_amount = self.request.POST.get('yield_amount')
        recipe.prep_time = self.request.POST.get('prep_time')
        recipe.ingredients = self.request.POST.get('ingredients')
        recipe.directions = self.request.POST.get('directions')
        recipe.image = self.request.POST.get('image')
        recipe.save()
        return HttpResponseRedirect(reverse('recipe_index'))


class RecipeDetailView(View):
    def get(self, request, pk=None):
        recipe = Recipe.objects.get(pk=pk)
        return render(request, 'recipes/recipe_detail.html', context={'recipe': recipe})


class RecipeDeleteView(View, ):
    def get(self, request, pk=None):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()
        return HttpResponseRedirect(reverse('recipe_index'))

    #
    pass
