from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('you_are_logged_in/', views.you_are_loged_in, name='logged_in'),
]
