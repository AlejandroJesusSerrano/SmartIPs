from django.urls import path
from smartipnav import views

urlpatterns = [
    path('index', views.index, name="Inicio"),
    path('printers', views.printers, name="Printers"),
    path('printer_add', views.printer_formm, name="AddPrinter"),
    path('computers', views.computer, name="Computers"),
    path('ip', views.ip, name="Ip"),
    path('userspc', views.userspc, name="UsersPc"),
    path('offices', views.office, name="Offices"),
    path('users', views.users, name="Users"),
]