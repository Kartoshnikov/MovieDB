from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.template import loader

# Create your views here.

from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import Movie, Person


class MovieList(ListView):
    model = Movie
    paginate_by = 10


class MovieDetail(DetailView):
    # model = Movie
    queryset = Movie.objects.all_with_related_persons()


class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()

