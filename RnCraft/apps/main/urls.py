from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('rules', views.rules, name = 'rules'),
    path('podderzhka', views.podderzhka, name = 'podderzhka'),
    path('pravila_administrirovania', views.pravila_administrirovania, name = 'pravila_administrirovania'),
    path('bedwars', views.bedwars, name = 'bedwars'),
    path('murdermystery', views.murdermystery, name = 'murdermystery'),
    path('keysi', views.keysi, name = 'keysi'),
    path('razban', views.razban, name = 'razban'),
    path('zuzcoin', views.zuzcoin, name = 'zuzcoin'),
    path('termini', views.termini, name='termini'),
    path('obzhie_pravila', views.obzhie_pravila, name='obzhie_pravila'),
    path('pravila_stroitelstva', views.pravila_stroitelstva, name='pravila_stroitelstva'),
    path('pravila_dla_donaterov', views.pravila_dla_donaterov, name='pravila_dla_donaterov'),
    path('pravila_obzhenia', views.pravila_obzhenia, name='pravila_obzhenia'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)