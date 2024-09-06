from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Sum
from django.db import models
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import *
from .utils import LocationMixin
from .forms import AddReserveForm, AddNewsForm

menu = [
    {'title': "Новости", 'url_name': 'news'},           # Позже добавить меню
        {'title': "Турниры", 'url_name': 'tournaments'},
        {'title': "Тренеры", 'url_name': 'trains'},
        {'title': "Бронь", 'url_name': 'reservation'},
        {'title': "Контакты", 'url_name': 'contacts'}
]

    #  === Классы для НОВОСТЕЙ ===
    
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
   
        # Добавление Новости
class AddNews(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = AddNewsForm
    template_name = 'courts/add_news.html'
    title_page = 'Добавление новости'
    permission_required = 'courts.add_news' # <приложение>.<действие>_<таблица>
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        res = form.save(commit=False)
        #messages.success(self.request, "The news was created successfully.")
        #res.user_id = self.request.user
        return super().form_valid(form)
    
    # Редактирование Новости
class EditNews(PermissionRequiredMixin, UpdateView):
    model = News
    slug_url_kwarg = 'post_slug'
    fields = ['title', 'content', 'photo', 'is_published']
    template_name = 'courts/add_news.html'
    title_page = 'Редактирование новости'
    permission_required = 'courts.change_news'
    success_url = reverse_lazy('news')

    #  === Классы для Местоположения ===

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
    context_object_name = 'location'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['location'].name
        #context['menu'] = menu
        #context['something'] =Location.objects.filter(pk=self.kwargs.get('post_id'))
        return context
    
    def get_object(self, queryset=None):
        return get_object_or_404(Location.objects.filter(pk=self.kwargs.get('loc_id')))
    

#  === Классы для ТУРНИРОВ ===
    
class TournamentList(ListView):
    model = Tournament
    template_name = 'courts/show_tournaments.html'
    context_object_name = 'tournaments'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Турниры"
        context['status']=self.kwargs['stat']
        return context
    
    def get_queryset(self):
        return Tournament.objects.all().filter(is_active=self.kwargs['stat'])

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


#  === Классы для ТРЕНЕРОВОК ===
  
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
    
#  === Классы для Аренд ===

class CourtsList(LocationMixin, ListView):
    model = Court
    template_name = 'courts/show_courts.html'
    context_object_name = 'courts'
    loc_selected = 0

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Аренда"
        return context

'''
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
'''
class CourtReserve(LoginRequiredMixin, CreateView): 
    model = Reserve   
    form_class = AddReserveForm
    template_name = 'courts/court.html'
    title_page = 'Добавление брони'
    permission_required = 'courts.add_reserve' # <приложение>.<действие>_<таблица>
    success_url = reverse_lazy('courts')       # Проверить!!! должно перенаправляться GetURL модели Reserve
    
    def form_valid(self, form):
        res = form.save(commit=False)
        res.user_id = self.request.user
        #res.court_id = Court.objects.filter(pk=self.kwargs.get('court_id'))
        '''
        перенесено в FORM
        q_reserve = Reserve.objects.filter(date_reserve = res.date_reserve, time_reserve = res.time_reserve, court_id = res.court_id)
        q_court = Court.objects.get(pk = res.court_id.pk)
        free_space = q_court.capacity - q_reserve.aggregate(Sum('quantity'))['quantity__sum'] - res.quantity
        free_space2 = q_court.capacity - q_reserve.aggregate(Sum('quantity'))['quantity__sum']

        #print(f'Записей на {res.date_reserve} {res.time_reserve} - {q_reserve.count()}. {q_reserve.aggregate(Sum('quantity'))['quantity__sum']} игроков + {res.quantity}')
        #print(f'Всего мест на корте - {q_court.capacity}')   #.values_list('capacity', flat=True)
        print(f'Было - {free_space2}; Осталось {free_space}')
        #if free_space < 0:              # ПРОВЕРКА НА СВОБОДНЫЕ МЕСТА  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #    form.add_error(None, 'Недостаточно свободных мест')
        
        '''
        return super().form_valid(form)
    
    def get_object(self, queryset=None):
        return get_object_or_404(Court.objects.filter(pk=self.kwargs.get('court_id')))
    

    #  === Классы для Брони ===
class ReservesList(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Reserve
    template_name = 'courts/show_reserves.html'
    context_object_name = 'reserves'
    permission_required = 'courts.view_reserve'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Бронь"
        return context

    # Добавление брони
class AddReserve(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = AddReserveForm
    template_name = 'courts/add_reserve.html'
    title_page = 'Добавление брони'
    permission_required = 'courts.add_reserve' # <приложение>.<действие>_<таблица>
    #success_url = reverse_lazy('courts')       # Проверить!!! должно перенаправляться GetURL модели Reserve
    '''
    def form_valid(self, form):
        Reserve.objects.create(**form.cleaned_data)
        return super().form_valid(form)
    '''
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
class CourtLocation (LocationMixin, ListView):
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
    

class AddReserve2(DetailView):                # TEST without Form

    model = Court
    template_name = 'courts/court_test.html'
    context_object_name = 'courts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Аренда"
        return context
