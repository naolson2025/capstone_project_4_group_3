from django.shortcuts import render

# Create your views here.

def weather_list(request):
    return render(request, 'party_templates/home.html')