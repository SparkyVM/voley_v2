from django.shortcuts import get_object_or_404, render
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .utils import DataMixin
from .forms import AddReserveForm

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
    status_selected = 1

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
'''
# НОВЫЙ КОД
class TournamentStatus(ListView):
    template_name = 'courts/show_tournaments.html'
    context_object_name = 'tournaments'
    allow_empty = False

    def get_queryset(self):
        return Tournament.active.filter(status__id=self.kwargs['status_id']).select_related("status")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = context['tournament'][0].cat
        return self.get_mixin_context(context,
                                      title='Категория - ' + cat.name,
                                      cat_selected=cat.pk,
                                      )
'''

    
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
    cat_selected = 0

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
    
    # Классы для Брони
class ReservesList(ListView):
    model = Reserve
    template_name = 'courts/show_reserves.html'
    context_object_name = 'reserves'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Бронь"
        return context
    
    # Добавление брони
class AddReserve(CreateView):
    form_class = AddReserveForm
    template_name = 'courts/add_reserve.html'
    title_page = 'Добавление брони'
    permission_required = 'courts.add_reserve' # <приложение>.<действие>_<таблица>
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        res = form.save(commit=False)
        res.user_id = self.request.user
        return super().form_valid(form)
    '''
    model = Court
    template_name = 'courts/show_courts.html'
    context_object_name = 'courts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Аренда"
        return context
    '''
    
    
    # Фильтр Кортов по Местоположению
class CourtLocation (DataMixin, ListView):
    template_name = 'courts/show_courts.html'
    context_object_name = 'courts'
    allow_empty = False

    def get_queryset(self):
        return Court.objects.all().filter(location__id=self.kwargs['loc_id']).select_related("location")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loc = context['courts'][0].location
        return self.get_mixin_context(context,
                                      title='Местоположение - ' + loc.name,
                                      loc_selected=loc.pk,
                                      )
