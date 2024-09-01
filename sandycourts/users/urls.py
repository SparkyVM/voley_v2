from django.urls import path
#from .views import *
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
]