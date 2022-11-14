from django.urls import path
from smartipnav import views

urlpatterns = [
    path('index', views.index, name="Inicio"),
    path('printers', views.printers, name="Printers"),
    path('printer_add', views.printer_form, name="AddPrinter"),
    path('computers', views.computer, name="Computers"),
    path('printer_add', views.computer_form, name="AddComputer"),
    path('ip', views.ip, name="Ip"),
    path('printer_add', views.ip_form, name="AddIp"),
    path('userspc', views.userspc, name="UsersPc"),
    path('printer_add', views.userspc_form, name="AddUserPc"),
    path('offices', views.office, name="Offices"),
    path('printer_add', views.office_form, name="AddOffice"),
    path('users', views.users, name="Users"),
    path('printer_add', views.user_form, name="AddUser"),
]