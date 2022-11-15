from django.shortcuts import render
from smartipnav.models import *
from smartipnav.forms import UsersPcForm

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
    



def userpc(request):
    return render(request, "smartipnav/userpc.html")

def userpc_result(request):
    
    userpc_name = request.GET["name_userpc"]
    userpc_searched = Userspc.objects.filter(name__icontains=userpc_name)
    
    return render(request, "smartipnav/userpc_search_result.html", {"userpc_searched":userpc_searched})
 




def userspc_form(request):
    
    if request.method == "POST":
        
        form = UsersPcForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            
            userspc = Userspc(name=data["nombre"], lastname=data["apellido"], pc_username=data["nombre_usuario_pc"], pc_name=data["nombre_pc"])

            userspc.save()
            
    form = UsersPcForm()
    return render(request, "smartipnav/userspc_form.html", {"form":form})






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

