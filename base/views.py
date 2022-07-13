from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

projects = [
    {"id" : 1, "name" : "Flyer evenement"},
    {"id" : 2, "name" : "Activité politique"},
    {"id" : 3, "name" : "Royal Fleur"}
]
def home(request) :
    return render(request, 'base/home.html')

def project(request) :
    context = {'projects' : projects}
    return render(request, 'base/project.html',{'projects' : context} )