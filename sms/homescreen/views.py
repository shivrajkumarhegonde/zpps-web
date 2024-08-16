from django.shortcuts import render

def home(request):
    return render(request, 'homescreen/template/home.html')

