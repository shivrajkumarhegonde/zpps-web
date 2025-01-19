from django.shortcuts import render, redirect
from .models import MidDayMeal
from django.contrib.auth.decorators import login_required

def meal_list(request):
    meals = MidDayMeal.objects.all()
    return render(request, 'mdm/template/meal_list.html', {'meals': meals})

@login_required
def meal_add(request):
    if request.method == 'POST':
        # Process form submission here
        pass
    return render(request, 'mdm/template/meal_form.html')

@login_required
def meal_edit(request, pk):
    # Process form submission for editing an existing record here
    pass

@login_required
def meal_delete(request, pk):
    # Process deletion of a meal record
    pass
