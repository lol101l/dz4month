from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('movies/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
    path('movies/new/', views.movie_create, name='movie_create'),
    path('users/', views.user_list, name='user_list'),
]