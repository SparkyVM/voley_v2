from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace="users")),
    path('', include('courts.urls')),
    #TemplateView.as_view(template_name='home.html'), name='home'),
    #path('info/', include('newsapp.urls')),
    #path('game/', include('gameapp.urls')),
    
]
