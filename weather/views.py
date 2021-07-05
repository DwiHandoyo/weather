
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

def getData(location):
    response = request.get('https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=-0.25 ')
    return response['geometry']['coordinates']

def home(request):
    if request.method == 'POST':
        location = request.POST['location']
        coordinate = getData(location)
    context = {
        'location' : location
    }
    return render(request,"index.html",context)
