from django.urls import path
from smartipnav.views import *

urlpatterns = [
    path('index', index, name="Inicio"),
    
    path('printers', printers, name="Printers"),
    path('printer_add', printer_form, name="AddPrinter"),
    path('printers_show', printers_list, name="PrintersList"),
    
    path('computers', computer, name="Computers"),
    path('computer_add', computer_form, name="AddComputer"),
    path('computers_show', computers_list, name="ComputersList"),
    
    path('ip', ip, name="Ip"),
    path('ip/ipsearch', ip_search_result, name="IpResult"),
    path('ip_add', ip_form, name="AddIp"),
    path('ips_show', ips_list, name="IpsList"),
    
    path('userpc', userpc, name="UserPc"),
    path('userpc/userpc_result', userpc_result, name='UserPcResult'),
    path('userpc_add', userspc_form, name="AddUserPc"),
    path('userspc_show', userspc_list, name="UserspcList"),
    
    path('offices', office, name="Offices"),
    path('offices/search_result', office_search_result, name="OfficeResult"),
    path('office_add', office_form, name="AddOffice"),
    path('offices_show', offices_list, name="OfficesList"),
    
    path('user_add', user_form, name="AddUser"),
    path('users_show', users_list, name="UsersList"),
]