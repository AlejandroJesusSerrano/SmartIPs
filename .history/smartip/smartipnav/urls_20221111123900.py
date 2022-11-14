from django.urls import path
from smartipnav import views

urlpatterns = [
    path('index', views.index),
    path('printers', views.printers, name="Printers"),
    path('computers', views.computer, name="Computers"),
    path('ip', views.ip, name="Ip"),
    path('userspc', views.userspc, name="UsersPc"),
    path('offices', views.office, name="Offices"),
    path('users', views.users, name="Users"),
]