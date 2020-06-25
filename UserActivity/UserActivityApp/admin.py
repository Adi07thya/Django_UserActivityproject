

from django.contrib import admin
from .models import Member,ActivityPeriod
from django.db import models

@admin.register(Member)
class AdminModel(admin.ModelAdmin):
    list_display=['real_name']

@admin.register(ActivityPeriod)
class AdminModel(admin.ModelAdmin):
    list_display=['start']
