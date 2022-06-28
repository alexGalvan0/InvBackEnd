from statistics import mode, quantiles
from tabnanny import check
from typing import TYPE_CHECKING
from django.shortcuts import render
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your views here.
class Team(models.Model):
    team_name = models.CharField(max_length=255)

class Types(models.Model):
    type_name = models.CharField(max_length=255)
    team = models.ForeignKey(Team,default=None)

class Items(models.Model):
    item_name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, default=None)
    total_qty = models.IntegerField()
    taken_qty = models.IntegerField()
    picture = models.ImageField()

class Custom_user(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email =  models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    team = models.ForeignKey(Team, default=None)
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

