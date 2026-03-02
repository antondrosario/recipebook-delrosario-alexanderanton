from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Ingredient, Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})

def ingredient_detail(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    return render(request, "ledger/ingredient_detail.html", {"ingredient": ingredient})