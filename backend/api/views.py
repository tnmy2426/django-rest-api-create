from django.shortcuts import render
from .serializers import MovieSerializer
from .models import Movie

# For ViewSet
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()