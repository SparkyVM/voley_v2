from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from sandycourts import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace="users")),
    path('', include('courts.urls')),
    #TemplateView.as_view(template_name='home.html'), name='home'),
    #path('info/', include('newsapp.urls')),
    #path('game/', include('gameapp.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)