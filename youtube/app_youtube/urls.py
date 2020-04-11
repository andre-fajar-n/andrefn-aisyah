from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'app_youtube'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:video_id>/', views.video_open, name='video_open'),
    path('search/', views.videos, name='search'),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)