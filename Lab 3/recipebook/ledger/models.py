from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinLengthValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField(validators=[MinLengthValidator(256)])

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient_detail", kwargs={"pk": self.pk})

class Recipe(models.Model):
    name = models.CharField(max_length=150, unique=True)

    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="recipes")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("recipe_detail", kwargs={"pk": self.pk})


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)

    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe"
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )

    def __str__(self) -> str:
        return f"{self.quantity} {self.ingredient.name} for {self.recipe.name}"