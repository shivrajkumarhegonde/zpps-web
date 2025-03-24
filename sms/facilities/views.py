from django.shortcuts import render, get_object_or_404, redirect
from .models import Facility
from .forms import FacilityForm
from django.contrib.auth.decorators import login_required

def facilities_view(request):
    return render(request, 'facilities/template/facilities.html')


def facilities_list(request):
    facilities = Facility.objects.all()
    return render(request, 'facilities/template/facilities_list.html', {'facilities': facilities})

@login_required
def add_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('facilities_list')
    else:
        form = FacilityForm()
    return render(request, 'facilities/template/add_facility.html', {'form': form})

@login_required
def update_facility(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('facilities_list')
    else:
        form = FacilityForm(instance=facility)
    return render(request, 'facilities/template/update_facility.html', {'form': form})

@login_required
def delete_facility(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == 'POST':
        facility.delete()
        return redirect('facilities_list')
    return render(request, 'facilities/template/delete_facility.html', {'facility': facility})