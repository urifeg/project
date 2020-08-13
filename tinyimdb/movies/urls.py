from django.urls import path
from . import views
appname = 'movies'
urlpatterns = [
    path('', views.movies_list, name='list'),
    path('<slug:slug>/', views.movie_detail, name='detail')
]
