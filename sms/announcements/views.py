# announcements/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Announcement
from .forms import AnnouncementForm

def announcements(request):
    announcements_list = Announcement.objects.all().order_by('-created_at')
    return render(request, 'announcements/template/announcements.html', {'announcements': announcements_list})

@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/template/announcement_form.html', {'form': form})

@login_required
def edit_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'announcements/template/announcement_form.html', {'form': form})

@login_required
def delete_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcements')
    return render(request, 'announcements/template/announcement_confirm_delete.html', {'announcement': announcement})
