# activities/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Activity, ActivityImage
from .forms import ActivityForm, ActivityImageFormSet

def activity_list(request):
    activities = Activity.objects.prefetch_related('images').all()
    return render(request, 'activities/template/activity_list.html', {'activities': activities})

@login_required
def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        formset = ActivityImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            activity = form.save()
            images = formset.save(commit=False)
            for image in images:
                image.activity = activity
                image.save()
            return redirect('activity_list')
    else:
        form = ActivityForm()
        formset = ActivityImageFormSet()

    return render(request, 'activities/template/create_activity.html', {
        'form': form,
        'formset': formset,
    })

@login_required
def edit_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES, instance=activity)
        formset = ActivityImageFormSet(request.POST, request.FILES, instance=activity)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('activity_list')
    else:
        form = ActivityForm(instance=activity)
        formset = ActivityImageFormSet(instance=activity)
    return render(request, 'activities/template/edit_activity.html', {'form': form, 'formset': formset})

@login_required
def delete_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('activity_list')
    return render(request, 'activities/template/delete_activity.html', {'activity': activity})
