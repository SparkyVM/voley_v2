from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display =['title', 'content', 'date_create', 'is_published']
    ordering = ['date_create']
    search_fields = ['title', 'content']
    search_help_text = 'Поиск в новостях'

admin.site.register(News, NewsAdmin)


class LocationsAdmin(admin.ModelAdmin):
    list_display =['name', 'adress', 'phone_number']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'

admin.site.register(Location, LocationsAdmin)

class CourtsAdmin(admin.ModelAdmin):
    list_display =['court_number', 'location', 'capacity']
    ordering = ['location', 'court_number']

admin.site.register(Court, CourtsAdmin)

class TournamentAdmin(admin.ModelAdmin):
    list_display =['date', 'title', 'comands_quantity', 'is_active']
    ordering = ['date']
    search_fields = ['title']
    search_help_text = 'Поиск турнира'
    list_editable = ['is_active']

admin.site.register(Tournament, TournamentAdmin)

class TrainerAdmin(admin.ModelAdmin):
    list_display =['last_name', 'first_name', 'location']
    ordering = ['last_name']
    search_fields = ['last_name', 'first_name']
    search_help_text = 'Поиск тренера'

admin.site.register(Trainer, TrainerAdmin)
