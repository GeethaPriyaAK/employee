from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'geetha'})

def add(request):
    res = 'pass'
    return render(request,'result.html',{'result':res})
     
