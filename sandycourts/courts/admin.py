from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display =['title', 'content', 'date_create', 'is_published']
    ordering = ['date_create']
    search_fields = ['title', 'content']
    search_help_text = 'Поиск в новостях'
    list_editable = ['is_published']

admin.site.register(News, NewsAdmin)


class LocationsAdmin(admin.ModelAdmin):
    list_display =['name', 'adress', 'phone_number']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'

admin.site.register(Location, LocationsAdmin)

class CourtAdmin(admin.ModelAdmin):
    list_display =['court_number', 'location', 'capacity']
    ordering = ['location', 'court_number']

admin.site.register(Court, CourtAdmin)

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

class ReserveAdmin(admin.ModelAdmin):
    list_display =['date_reserve', 'time_reserve', 'court_id', 'quantity', 'user_id']
    ordering = ['-date_reserve']

admin.site.register(Reserve, ReserveAdmin)