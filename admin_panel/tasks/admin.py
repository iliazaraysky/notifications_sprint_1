from django.contrib import admin
from .models import Templates, Tasks


@admin.register(Templates)
class AdminTemplates(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'created_at')


@admin.register(Tasks)
class AdminTemplates(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'status', 'created_at')
