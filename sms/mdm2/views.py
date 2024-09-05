from django.shortcuts import render, redirect, get_object_or_404
from .models import MidDayMeal
from .forms import MidDayMealForm
from django.contrib.auth.decorators import login_required

def meal_list(request):
    meals = MidDayMeal.objects.all()
    return render(request, 'mdm2/template/meal_list.html', {'meals': meals})

@login_required
def meal_add(request):
    if request.method == "POST":
        form = MidDayMealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal_list')  # Redirect to meal list after adding a meal
    else:
        form = MidDayMealForm()

    return render(request, 'mdm2/template/meal_form.html', {'form': form})

@login_required
def meal_edit(request, pk):
    meal = get_object_or_404(MidDayMeal, pk=pk)
    if request.method == "POST":
        form = MidDayMealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('meal_list')  # Redirect to meal list after editing a meal
    else:
        form = MidDayMealForm(instance=meal)

    return render(request, 'mdm2/template/meal_form.html', {'form': form})

@login_required
def meal_confirm_delete(request, pk):
    meal = get_object_or_404(MidDayMeal, pk=pk)
    if request.method == "POST":
        meal.delete()
        return redirect('meal_list')  # Redirect to meal list after deleting a meal
    return render(request, 'mdm2/template/meal_confirm_delete.html', {'meal': meal})
