from django.shortcuts import render

# Create your.htmls here.

def index(request):
    return render(request, "smartipnav/index.html")

def printers(request):
    return render(request, "smartipnav/printers.html")

def computer(request):
    return render(request, "smartipnav/computers.html")
    
def ip(request):
    return render(request, "smartipnav/ip.html")
    
def userspc(request):
    return render(request, "smartipnav/userspc.html")

def office(request):
    return render(request, "smartipnav/office.html")

def users(request):
    return render(request, "smartipnav/users.html")

