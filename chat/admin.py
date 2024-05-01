from django.contrib import admin
from .models import ChatGroup, Message, Profile
# Register your models here.
admin.site.register([ChatGroup, Message, Profile])