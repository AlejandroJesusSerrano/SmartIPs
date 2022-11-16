from django.shortcuts import render
from smartipnav.models import *
from smartipnav.forms import UsersPcForm, OfficeForm, IpForm

# Create your.htmls here.
#*INDEX VIEW
def index(request):
    return render(request, "smartipnav/index.html")

#*PRINTERS VIEWS
def printers(request):
    return render(request, "smartipnav/printers.html")
def printer_form(request):
    return render(request, "smartipnav/printer_form.html")
def printers_list(request):
    return render(request, "smartipnav/printers_list.html")

#*COMPUTERS VIEWS
def computer(request):
    return render(request, "smartipnav/computer.html")
def computer_form(request):
    return render(request, "smartipnav/computer_form.html")
def computers_list(request):
    return render(request, "smartipnav/computers_list.html")

#*IP´S VIEWS
#Ip search
def ip(request):
    return render(request, "smartipnav/ip.html")

def ip_search_result(request):
    
    dir_ip = request.GET["ip_dir"]
    ipdir_searched = Ip.objects.filter(ipdir__icontains=dir_ip)
    
    return render(request, "smartipnav/ip_search_result.html", {"ipdir_searched":ipdir_searched})

#Ip Add
def ip_form(request):
    
    if request.method == "POST":
        
        ip_add_form = IpForm(request.POST)
                
        if ip_add_form.is_valid():
            data = ip_add_form.cleaned_data
            
            ip = Ip(ipdir=data["direccion_ip"], device=data["equipo"], internet=data["internet_acceso_libre"] )

            ip.save()
            
    ip_add_form = IpForm()
    return render(request, "smartipnav/ip_form.html", {"ip_add_form":ip_add_form})

#Ip List
def ips_list(request):
    ip_listed = Ip.objects.all()
    return render(request, "smartipnav/ips_list.html", {"ip_listed":ip_listed})   


#*USERS PC VIEWS
#Userspc search
def userpc(request):
    return render(request, "smartipnav/userpc.html")

def userpc_result(request):
    
    userpc_name = request.GET["name_userpc"]
    userpc_searched = Userspc.objects.filter(name__icontains=userpc_name)
    
    return render(request, "smartipnav/userpc_search_result.html", {"userpc_searched":userpc_searched})

# Userspc Add
def userspc_form(request):
    
    if request.method == "POST":
        
        form = UsersPcForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            
            userspc = Userspc(name=data["nombre"], lastname=data["apellido"], pc_username=data["nombre_usuario_pc"], pc_name=data["nombre_pc"])

            userspc.save()
            
    form = UsersPcForm()
    return render(request, "smartipnav/userspc_form.html", {"form":form})

#List all Userspc
def userspc_list(request):
    pc_users = Userspc.objects.all()
    return render(request, "smartipnav/userspc_list.html", {"pc_users":pc_users})


#* OFFICES VIEWS
# Offices search
def office(request):
    return render(request, "smartipnav/office.html")

def office_search_result(request):
    
    office_judge = request.GET["judge"]
    offices_searched = Office.objects.filter(judge__icontains=office_judge)
    
    return render(request, "smartipnav/office_result.html", {"offices_searched":offices_searched})

#office Add
def office_form(request):
    
    if request.method == "POST":
        
        form_office = OfficeForm(request.POST)

        if form_office.is_valid():
            data = form_office.cleaned_data
            
            office = Office(officename=data["oficina"], location=data["edificio"], judge=data["juzgado"], floor=data["piso"])

            office.save()
            
    form_office = OfficeForm()
    return render(request, "smartipnav/office_form.html", {"form_office":form_office})

#list all offices
def offices_list(request):
    offices_list = Office.objects.all()
    return render(request, "smartipnav/offices_list.html",{"offices_list":offices_list})


#SYSTEM USERS VIEWS
def users(request):
    return render(request, "smartipnav/users.html")
def user_form(request):
    return render(request, "smartipnav/user_form.html")
def users_list(request):
    return render(request, "smartipnav/users_list.html")

