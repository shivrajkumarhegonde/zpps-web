from django.shortcuts import render

def facilities_view(request):
    return render(request, 'facilities/template/facilities.html')
