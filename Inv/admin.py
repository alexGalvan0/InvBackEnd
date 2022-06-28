from django.contrib import admin
from .models import Team,Custom_user,Item,ItemType

# Register your models here.
admin.site.register(Team)
admin.site.register(Custom_user)
admin.site.register(ItemType)
admin.site.register(Item)