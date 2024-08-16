from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import FacultyMember
from .forms import FacultyMemberForm

def faculty_list(request):
    faculties = FacultyMember.objects.all()
    return render(request, 'zpps_faculty/template/faculty_list.html', {'faculties': faculties})

def create_faculty(request):
    if request.method == 'POST':
        form = FacultyMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyMemberForm()
    return render(request, 'zpps_faculty/template/faculty_form.html', {'form': form})

def update_faculty(request, faculty_id):
    faculty = get_object_or_404(FacultyMember, id=faculty_id)
    if request.method == 'POST':
        form = FacultyMemberForm(request.POST, request.FILES, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyMemberForm(instance=faculty)
    return render(request, 'zpps_faculty/template/faculty_form.html', {'form': form})


def delete_faculty(request, faculty_id):
    faculty = get_object_or_404(FacultyMember, id=faculty_id)
    if request.method == 'POST':
        faculty.delete()
        messages.success(request, 'Faculty member deleted successfully')
        return redirect('faculty_list')
    return render(request, 'zpps_faculty/template/faculty_confirm_delete.html', {'faculty': faculty})