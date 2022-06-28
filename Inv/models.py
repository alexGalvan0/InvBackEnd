from email.policy import default
from operator import mod
from django.db import models
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

#Create Team Model
class Team (models.Model):
    team_name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.team_name


#Create the user Model
class Custom_user(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email =  models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    team = models.ForeignKey(Team, default=None, on_delete=models.CASCADE)
    username = None
    #is_superuser = None
    #is_staff = None
    groups = None
    user_permissions = None
    last_login = None

    AUTH_USER_MODEL = 'account.user'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
            return self.first_name


#Item Types
class ItemType(models.Model):
    item_type_name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,null=True)
    def __str__(self):
            return self.item_type_name



#Item
class Item (models.Model):
    item_name = models.CharField(max_length=255)
    ItemType =models.ForeignKey(ItemType, on_delete=models.CASCADE)
    team = models.ForeignKey(Team,default=None, on_delete=models.CASCADE, null=True)
    total_qty = models.IntegerField()
    taken_qty = models.IntegerField()
    item_picture = models.ImageField(default=None, null=True, blank=True)
    def __str__(self):
            return self.item_name