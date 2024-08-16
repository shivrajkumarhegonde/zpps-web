from django.shortcuts import render

def achievements(request):
    return render(request, 'achievements/template/achievements.html')