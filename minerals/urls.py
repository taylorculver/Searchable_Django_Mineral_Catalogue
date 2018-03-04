from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'minerals'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('letter/<letter>', views.letter, name='letter'),
    path('group/<group>/', views.group, name='group'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
