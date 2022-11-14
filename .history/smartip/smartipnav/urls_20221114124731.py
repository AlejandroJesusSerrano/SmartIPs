from django.urls import path
from smartipnav import views

urlpatterns = [
    path('index', views.index, name="Inicio"),
    
    path('printers', views.printers, name="Printers"),
    path('printer_add', views.printer_form, name="AddPrinter"),
    path('printers_show', views.printers_list, name="PrintersList"),
    
    path('computers', views.computer, name="Computers"),
    path('computer_add', views.computer_form, name="AddComputer"),
    path('computers_show', views.computers_list, name="ComputersList"),
    
    path('ip', views.ip, name="Ip"),
    path('ip_add', views.ip_form, name="AddIp"),
    path('ips_show', views.ips_list, name="IpsList"),
    
    path('userspc', views.userspc, name="UsersPc"),
    path('userpc_add', views.userspc_form, name="AddUserPc"),
    path('userspc_show', views.userspc_list, name="UserspcList"),
    
    path('offices', views.office, name="Offices"),
    path('office_add', views.office_form, name="AddOffice"),
    path('offices_show', views.offices_list, name="OfficesList"),
    
    path('users', views.users, name="Users"),
    path('user_add', views.user_form, name="AddUser"),
    path('users_show', views.users_list, name="UsersList"),
]