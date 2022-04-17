from django.urls import path
from . import views

urlpatterns = [
    path('projAbout/', views.projAbout, name='ScheduleDeck-projAbout'),
    path('projHome/', views.projHome, name='ScheduleDeck-projHome'),
    path('', views.index, name='ScheduleDeck-index'),
    path("simple_function/", views.simple_function),
    path("result/", views.result, name='ScheduleDeck-result')
]