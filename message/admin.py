from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass