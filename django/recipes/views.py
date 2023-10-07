from django.shortcuts import render

from .forms import RecipeForm

from .models import recipe
# Create your views here.

def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RecipeForm()
    context = {
        'form': form
    }

    return render(request, "recipes_render.html", context)

def recipe_detail_view(request):
    obj = recipe.objects.get(id = 1)
    context = {
        'object' : obj
    }
    return render(request, "recipes/recipes_details.html" , context)