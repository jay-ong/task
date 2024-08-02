from django.urls import path
from .views import index, movies, sources

urlpatterns = [
    path('', index, name='index'),
    path('api/movies', movies, name='search_movie'),
    path('api/sources', sources, name='sources'),
]