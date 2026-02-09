from django.shortcuts import render

RECIPE_LIST_CONTEXT = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {"name": "tomato", "quantity": "3pcs"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "pork", "quantity": "1kg"},
                {"name": "water", "quantity": "1L"},
                {"name": "sinigang mix", "quantity": "1 packet"},
            ],
            "link": "/recipe/1",
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {"name": "garlic", "quantity": "1 head"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "vinegar", "quantity": "1/2cup"},
                {"name": "water", "quantity": "1 cup"},
                {"name": "soy sauce", "quantity": "1/2cup"},
                {"name": "peppercorn", "quantity": "1 tbsp"},
                {"name": "chicken", "quantity": "1kg"},
            ],
            "link": "/recipe/2",
        },
    ]
}

RECIPE_1_CONTEXT = {
    "name": "Recipe 1",
    "ingredients": [
        {"name": "tomato", "quantity": "3pcs"},
        {"name": "onion", "quantity": "1pc"},
        {"name": "pork", "quantity": "1kg"},
        {"name": "water", "quantity": "1L"},
        {"name": "sinigang mix", "quantity": "1 packet"},
    ],
}

RECIPE_2_CONTEXT = {
    "name": "Recipe 2",
    "ingredients": [
        {"name": "garlic", "quantity": "1 head"},
        {"name": "onion", "quantity": "1pc"},
        {"name": "vinegar", "quantity": "1/2cup"},
        {"name": "water", "quantity": "1 cup"},
        {"name": "soy sauce", "quantity": "1/2cup"},
        {"name": "peppercorn", "quantity": "1 tbsp"},
        {"name": "chicken", "quantity": "1kg"},
    ],
}

def recipe_list(request):
    return render(request, "ledger/recipe_list.html", RECIPE_LIST_CONTEXT)


def recipe_1(request):
    return render(request, "ledger/recipe_detail.html", RECIPE_1_CONTEXT)


def recipe_2(request):
    return render(request, "ledger/recipe_detail.html", RECIPE_2_CONTEXT)
