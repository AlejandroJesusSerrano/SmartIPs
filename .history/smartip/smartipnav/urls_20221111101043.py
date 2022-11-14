from django.urls import path
from smartipnav import views

urlpatterns = [
    path('', views.index),
    path('printers', views.printers, name="Printers"),
    path('computers', views.printers, name="Computers"),
    path('ip', views.printers, name="Ip"),
    path('userspc', views.printers, name="UsersPc"),
    path('offices', views.printers, name="Offices"),
    path('users', views.printers, name="Users"),
]