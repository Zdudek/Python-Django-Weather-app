# project level views
import datetime
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    """
    Test function, return Hello world
    """
    return HttpResponse("Hello world")
    #now = datetime.datetime.now()
    #html = "It is now %s." % now
    #return HttpResponse(html)
    
def home(request):
    """
    return: display the home page of weather app
    """
    context = {} 
    now = datetime.datetime.now()
    html = "It is now %s." % now
    context = {'data_time': html}
    return render(request, 'home.html', context)
