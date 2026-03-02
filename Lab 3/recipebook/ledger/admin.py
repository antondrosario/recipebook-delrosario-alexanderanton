from django.contrib import admin
from .models import Ingredient, Profile, Recipe, RecipeIngredient


# (optional but nice) show recipe ingredients inline when editing a recipe
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    search_fields = ("name", "user__username", "user__email")


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ("name", "author", "created_on", "updated_on")
    list_select_related = ("author",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# IMPORTANT:
# Do NOT add admin.site.register(Recipe) anywhere else,
# because @admin.register(Recipe) already registers it.