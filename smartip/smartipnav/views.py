from django.shortcuts import render
from smartipnav.models import Ip

# Create your.htmls here.

def index(request):
    return render(request, "smartipnav/index.html")

def printers(request):
    return render(request, "smartipnav/printers.html")
def printer_form(request):
    return render(request, "smartipnav/printer_form.html")
def printers_list(request):
    return render(request, "smartipnav/printers_list.html")

def computer(request):
    return render(request, "smartipnav/computer.html")
def computer_form(request):
    return render(request, "smartipnav/computer_form.html")
def computers_list(request):
    return render(request, "smartipnav/computers_list.html")

    
def ip(request):
    return render(request, "smartipnav/ip.html")
def ip_form(request):
    
    if request.method == "POST":
        ip_direction = request.POST["ipdir"]
                
        ip = Ip(ipdir=ip_direction)
        ip.save()

    return render(request, "smartipnav/ip_form.html")

def ips_list(request):
    return render(request, "smartipnav/ips_list.html")
    

def userspc(request):
    return render(request, "smartipnav/userspc.html")
def userspc_form(request):
    return render(request, "smartipnav/userspc_form.html")
def userspc_list(request):
    return render(request, "smartipnav/userspc_list.html")

def office(request):
    return render(request, "smartipnav/office.html")
def office_form(request):
    return render(request, "smartipnav/office_form.html")
def offices_list(request):
    return render(request, "smartipnav/offices_list.html")

def users(request):
    return render(request, "smartipnav/users.html")
def user_form(request):
    return render(request, "smartipnav/user_form.html")
def users_list(request):
    return render(request, "smartipnav/users_list.html")

