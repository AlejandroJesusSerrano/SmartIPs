from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def index(request):
    return HttpRequest("index view")

def printers(request):
    return HttpRequest("printers view")

def computer(request):
    return HttpRequest("computer view")
    
def ip(request):
    return HttpRequest("ip view")
    
def userspc(request):
    return HttpRequest("userspc view")

def office(request):
    return HttpRequest("office view")

def users(request):
    return HttpRequest("users view")

