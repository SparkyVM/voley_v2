from django.urls import path, include
from django.views.generic import TemplateView
from courts.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html', extra_context={"title": "SandyCourts"}), name='home'),
    path('about/', TemplateView.as_view(template_name='courts/about.html', extra_context={"title": "О нас"}), name='about'),

        # Новости
    path('news/', NewsList.as_view(), name='news'),
    path('news/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('news_add/', AddNews.as_view(), name='news_add'),
    path('news_edit/<slug:post_slug>/', EditNews.as_view(), name='news_edit'),
    # path('<slug:article_slug>/', ShowArticle.as_view(), name='article'),

        # Контакты
    path('contacts/', LocationList.as_view(), name='contacts'),
    path('contacts/<int:loc_id>', ShowLocation.as_view(), name='location'),

        # Турниры
    path('tournaments/<int:stat>/', TournamentList.as_view(), name='tournaments'),
    path('tournaments_res/<slug:tournament_slug>/', ShowTournament.as_view(), name='tnmt_res'), 

        # Тренеровка
    path('trains/', TrainerList.as_view(), name='trains'),
    path('trains/<int:trainer_id>/', ShowTrainer.as_view(), name='train'),

        # Аренда
    path('courts/', CourtsList.as_view(), name='courts'),
    path('courts/<int:court_id>/', CourtReserve.as_view(), name='court'),      # Нужен ли
    path('location/<int:loc_id>/', CourtLocation.as_view(), name='location'),

    path('res/', ReservesList.as_view(), name='res'),
    path('addres/', AddReserve.as_view(), name='addres'),
    path('addres2/', AddReserve2.as_view(), name='addres2'),

    
    
]
