import django
from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='recipe_index'),
    path('recipes/', views.RecipeListView.as_view(), name='recipes_recipe_list'),
    path('recipes/add/', views.RecipeAddView.as_view(), name='recipes_recipe_add'),
    path('recipes/<int:pk>/edit/', views.RecipeEditView.as_view(), name='recipes_recipe_edit'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipes_recipe_delete'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipes_recipe_detail'),
]