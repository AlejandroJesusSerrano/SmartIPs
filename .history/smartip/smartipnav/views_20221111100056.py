from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("index view")

def printers(request):
    return HttpResponse("printers view")

def computer(request):
    return HttpResponse("computer view")
    
def ip(request):
    return HttpResponse("ip view")
    
def userspc(request):
    return HttpResponse("userspc view")

def office(request):
    return HttpResponse("office view")

def users(request):
    return HttpResponse("users view")

