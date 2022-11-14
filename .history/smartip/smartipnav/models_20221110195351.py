from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)

class Ip(models.Model):
        ipdir = models.CharField(max_length=13)

class Office(models.Model):
        officename = models.CharField(max_length=30)
        floor = models.CharField(max_length=3)

class Userspc(models.Model):
        name = models.CharField(max_length=30)
        lastname = models.CharField(max_length=30)
        pc_username = models.CharField(max_length=6)
        pc_name = models.CharField(max_length=8)

class Computer(models.Model):
        image = models.ImageField()
        model = models.CharField(max_length=10)
        brand = models.CharField(max_length=15)
        rebuilded = models.BooleanField(default=False)
        ip = models.ForeignKey(Ip, on_delete=models.CASCADE)
        reg_user = models.ForeignKey(Userspc, on_delete=models.CASCADE)
        Office = models.ForeignKey(Office, on_delete=models.CASCADE)

class Printer(models.Model):
        image = models.ImageField()
        model = models.CharField(max_length=10)
        brand = models.CharField(max_length=15)
        rebuilded = models.BooleanField(default=False)
        ip = models.ForeignKey(Ip, on_delete=models.CASCADE)
        Office = models.ForeignKey(Office, on_delete=models.CASCADE)