#WEATHER VIEW.PY
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from collections import OrderedDict
from . models import Location
import urllib.request
import json

# Create your views here.
def home(request):
    """
    return: display the home page of weather app
    """
    context = {}
    your_city_name =''
    if request.method == 'POST':        
        your_city_name = request.POST.get('city_name')     
        userData = city_weather(your_city_name)               
    if (your_city_name ==''):
        return render(request, 'weather/home.html', context)
    else:
        return render_to_response('weather/home.html',{'data': userData})

def forecast(request):
    """
    return: display the forecast of a city
    """   
    context = {}     
    your_city_name = 'Pyaozerskiy'
    listDict = forecast_data(your_city_name) 
    if request.method == 'POST':
        your_city_name = request.POST.get('city_name')
        listDict = forecast_data(your_city_name)                  
    if (your_city_name =='Pyaozerskiy'):
        return render(request, 'weather/forecast.html', context)
    else:
        return render_to_response('weather/forecast.html',{'listDict': listDict})
    
def templete(request):
    """
    return: display the weather of all locations on our database in the weather app
    """
    q = Location.objects.all( )	
    length = len(q)
    listDict = []    
    for i in range (length):
        url='http://api.openweathermap.org/data/2.5/weather?id='+q[i].loc_city+'&units=imperial&appid=4b1c054c1fe5b2ba5d2f4a2f09e8fba0'
        jsonList = []
        request = urllib.request.Request(url) 
        response = urllib.request.urlopen(request)    
        response_body = response.read()   
        j = json.loads(response_body.decode("utf-8"))    
        jsonList.append(j)
        userData = OrderedDict()
        for data in jsonList:
            userData['City'] = data['name']           
            userData['Country'] = data['sys']['country']
            userData['Weather'] = data['weather'][0]['main']
            userData['Temp'] = data['main']['temp']            
            userData['Wind speed'] = data['wind']['speed']            
            userData['clouds'] = data['clouds']['all'] 
            userData['Pressure'] = data['main']['pressure'] 			
        listDict.append(userData)    
    return render_to_response('weather/temp.html',{'listDict': listDict})	
    
def forecast_data(city_name):
    """
    return: return the data of the forecast of a city from API
    """           
    key ='4b1c054c1fe5b2ba5d2f4a2f09e8fba0'
    url='http://api.openweathermap.org/data/2.5/forecast?q='+city_name+'&units=imperial&appid='+key
    
    request = urllib.request.Request(url) 
    response = urllib.request.urlopen(request)    
    response_body = response.read()   
    j = json.loads(response_body.decode("utf-8"))    
    listDict = [] 
    userData = OrderedDict()
    userData['City'] = j['city']['name']
    userData['Country'] = j['city']['country']  
    listDict.append(userData) 

    for i in (0,8,16,24,32):    
        userData = OrderedDict()
        userData['Time'] = j['list'][i]['dt_txt']
        userData['Weather'] = j['list'][i]['weather'][0]['main']
        userData['Temp'] = j['list'][i]['main']['temp']            
        userData['Wind speed'] = j['list'][i]['wind']['speed']            
        userData['clouds'] = j['list'][i]['clouds']['all'] 
        userData['Pressure'] = j['list'][i]['main']['pressure']
        listDict.append(userData)

    return listDict


def city_weather(city_name):
    """
    return: display the weather of a city
    """
    key ='4b1c054c1fe5b2ba5d2f4a2f09e8fba0'   
    url='http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&units=imperial&appid='+key
    jsonList = []
    request = urllib.request.Request(url) 
    response = urllib.request.urlopen(request)    
    response_body = response.read()   
    j = json.loads(response_body.decode("utf-8"))    
    jsonList.append(j)
    userData = OrderedDict()
    for data in jsonList:
        userData['City'] = data['name']
        userData['Country'] = data['sys']['country']
        userData['Weather'] = data['weather'][0]['main']
        userData['Temp'] = data['main']['temp']
        userData['Wind speed'] = data['wind']['speed'] 
        userData['clouds'] = data['clouds']['all'] 
        userData['Pressure'] = data['main']['pressure']    
    return userData

def list_all(request):
    """
    return: Display the data from our database to list_all.html pages.
    """
    q = Location.objects.all( )
    context = {'query':q}
    return render(request,'weather/list_all.html',context)
def about(request):
    """
    return: Display the information about us in about.html pages.
    """
    context = {}
    return render(request, 'weather/about.html', context)	
def add(request):    
    """
    Let users add more data to the dtatabase
    """
    context = {}
    if request.method == 'POST':
        print(request.POST)
        post_loc_city = request.POST.get('loc_city')
        post_city_name = request.POST.get('city_name')
        r = Location(loc_city = post_loc_city, city_name = post_city_name)
        r.save()
        context['success'] = True
    return render(request,'weather/add.html',context)
def manchester(request):
    """
    Display the current weather of Manchester
    """ 
    userData = weather_data('5000598')   
    return render_to_response('weather/manchester.html',{'data': userData})  
def boston(request):
    """
    Display the current weather of Boston
    """    
    userData = weather_data('4930956')    
    return render_to_response('weather/manchester.html',{'data': userData}) 
	
def nyc(request):
    """
    Display the current weather of New York City
    """
    userData = weather_data('5128581')
    return render_to_response('weather/manchester.html',{'data': userData}) 
def weather_data(id):
    """
    id: id of a city
    Return the current weather of that city
    """ 
    key ='4b1c054c1fe5b2ba5d2f4a2f09e8fba0'   
    url='http://api.openweathermap.org/data/2.5/weather?id='+id+'&units=imperial&appid='+key
    jsonList = []
    request = urllib.request.Request(url) 
    response = urllib.request.urlopen(request)    
    response_body = response.read()   
    j = json.loads(response_body.decode("utf-8"))    
    jsonList.append(j)
    userData = OrderedDict()
    for data in jsonList:
        userData['City'] = data['name']
        userData['Country'] = data['sys']['country']
        userData['Weather'] = data['weather'][0]['main']
        userData['Temp'] = data['main']['temp']
        userData['Wind speed'] = data['wind']['speed'] 
        userData['clouds'] = data['clouds']['all'] 
        userData['Pressure'] = data['main']['pressure']    
    return userData