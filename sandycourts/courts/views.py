from django.shortcuts import get_object_or_404, render
from django.db import models
from django.views.generic import ListView, DetailView 
from .models import *

menu = [
    {'title': "Новости", 'url_name': 'news'},           # Позже добавить меню
        {'title': "Турниры", 'url_name': 'tournaments'},
        {'title': "Тренеры", 'url_name': 'trains'},
        {'title': "Бронь", 'url_name': 'reservation'},
        {'title': "Контакты", 'url_name': 'contacts'}
]

    # Классы для Новостей
    
class NewsList(ListView):
    model = News
    template_name = 'courts/show_news.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):          # возможно не выполняется. Проверить
        context = super().get_context_data(**kwargs)
        context['title']="Страница новостей"
        return context
    
    def get_queryset(self):
        return News.published.all()
    
class ShowPost(DetailView):
    template_name = 'courts/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['menu'] = menu
        #context['something'] =News.objects.filter(pk=self.kwargs.get('post_id'))
        return context
    
    def get_object(self, queryset=None):
        return get_object_or_404(News.published, slug=self.kwargs[self.slug_url_kwarg])
   

    # Классы для Контактов

class LocationList(ListView):
    model = Location
    template_name = 'courts/locations.html'
    context_object_name = 'locations'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Локации"
        return context
    
class ShowLocation(DetailView):
    template_name = 'courts/location.html'
    #slug_url_kwarg = 'post_slug'
    context_object_name = 'location'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['location'].name
        context['menu'] = menu
        #context['something'] =Location.objects.filter(pk=self.kwargs.get('post_id'))
        return context
    
    def get_object(self, queryset=None):
        return get_object_or_404(Location.objects.filter(pk=self.kwargs.get('loc_id')))
    
# Классы для Турниров
    
class TournamentList(ListView):
    model = Tournament
    template_name = 'courts/show_tournaments.html'
    context_object_name = 'tournaments'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Турниры"
        return context

class ShowTournament(DetailView):
    template_name = 'courts/tournament.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'tournament'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['tournament'].title
        #context['menu'] = menu
        #context['something'] =News.objects.filter(pk=self.kwargs.get('post_id'))
        return context
    
    def get_object(self, queryset=None):
        return get_object_or_404(Tournament.objects.filter(slug=self.kwargs.get('tournament_slug')))

# Классы для Тренеровок
  
class TrainerList(ListView):
    model = Trainer
    template_name = 'courts/show_trainers.html'
    context_object_name = 'trainers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Тренеры"
        return context
    
class ShowTrainer(DetailView):
    template_name = 'courts/trainer.html'
    #slug_url_kwarg = 'post_slug'
    context_object_name = 'trainer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['trainer'].last_name
        #context['menu'] = menu
        #context['something'] =News.objects.filter(pk=self.kwargs.get('post_id'))
        return context
    
    def get_object(self, queryset=None):
        return get_object_or_404(Trainer.objects.filter(pk=self.kwargs.get('trainer_id')))
    
# Классы для Аренд

class CourtsList(ListView):
    model = Court
    template_name = 'courts/show_courts.html'
    context_object_name = 'courts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Аренда"
        return context
    
class ShowCourt(DetailView):
    template_name = 'courts/court.html'
    context_object_name = 'court'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['court'].court_number
        #context['menu'] = menu
        #context['something'] =News.objects.filter(pk=self.kwargs.get('post_id'))
        return context
    
    def get_object(self, queryset=None):
        return get_object_or_404(Court.objects.filter(pk=self.kwargs.get('court_id')))
    