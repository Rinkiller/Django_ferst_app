from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about_me, name='about_me'),
    path('coin/', views.coin, name='coin'),
    path('kub/', views.kub, name='kub'),
]