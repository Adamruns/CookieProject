from django.shortcuts import render
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

    # def post(self):
    #     return HttpResponse("Cool stuff")


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
        print(title, yield_amount)

        recipe = models.Recipe.objects.create(title=title, yield_amount=yield_amount, prep_time=prep_time,
         ingredients=ingredients, directions=directions)
        # recipe.title = title
        # recipe.yield_amount = yield_amount
        # recipe.save()
        #
        return HttpResponseRedirect(reverse('recipe_index'))


class RecipeEditView(View):
    pass


class RecipeDetailView(View):
    pass


class RecipeDeleteView(View):
    pass
