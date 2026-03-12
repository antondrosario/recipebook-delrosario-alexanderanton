from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView

from .forms import RecipeForm, RecipeImageForm
from .models import Ingredient, Recipe, RecipeImage


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})


def ingredient_detail(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    return render(request, "ledger/ingredient_detail.html", {"ingredient": ingredient})


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "ledger/recipe_form.html"

    def form_valid(self, form):
        profile = getattr(self.request.user, "profile", None)
        if profile is not None:
            form.instance.author = profile
        return super().form_valid(form)


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "ledger/recipeimage_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.recipe = get_object_or_404(Recipe, pk=self.kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.recipe = self.recipe
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = self.recipe
        return context

    def get_success_url(self):
        return self.recipe.get_absolute_url()