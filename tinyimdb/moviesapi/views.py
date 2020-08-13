from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from movies.models import Movie
from .serializers import MovieSerializer

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)