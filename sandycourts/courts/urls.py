from django.urls import path, include
from django.views.generic import TemplateView
from courts.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

        # Новости
    path('news/', NewsList.as_view(), name='news'),
    path('news/<slug:post_slug>/', ShowPost.as_view(), name='post'), 
    #path('<slug:article_slug>/', ShowArticle.as_view(), name='article'),

        # Контакты
    path('contacts/', LocationList.as_view(), name='contacts'),
    path('contacts/<int:loc_id>', ShowLocation.as_view(), name='location'),

        # Турниры
    path('tournaments/', TournamentList.as_view(), name='tournaments'), 
    path('tournaments/<slug:tournament_slug>/', ShowTournament.as_view(), name='tournament'), 
    #path('<slug:article_slug>/', ShowArticle.as_view(), name='article'),

        # Тренеровка
    path('trains/', TrainerList.as_view(), name='trains'),
    path('trains/<int:trainer_id>/', ShowTrainer.as_view(), name='train'),

        # Аренда
    path('courts/', CourtsList.as_view(), name='courts'),
    path('courts/<int:court_id>/', ShowCourt.as_view(), name='court'),
]
