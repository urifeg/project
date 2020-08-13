from django.shortcuts import render, HttpResponse
from .models import Movie

# Create your views here.
def movies_list(request):
    movies = Movie.objects.all().order_by('date')
    return render(request, 'movies/movies_list.html', {'movies':movies})

def movie_detail(request, slug):
    movie = Movie.objects.get (slug=slug)
    return render(request, "movies/movie_detail.html", {'movie':movie})