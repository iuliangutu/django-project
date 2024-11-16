from django.shortcuts import render
from datetime import date

# Create your views here.
from django.http import HttpResponse

from viewer.models import Movie, Genre
from django.urls import resolve


def home(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    rating = request.GET.get('rating', '')
    if rating:
        movies = movies.filter(rating__gt=rating)

    an = request.GET.get('an', '')
    if an:
        an = int(an)
        d = date(an, 1, 1)
        movies = movies.filter(released__gt=d)

    return render(
        request, template_name='home.html',
        context={'movies': movies, 'genres': genres})

def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)

    return render(
        request, template_name='movie.html',
        context={'movie': movie}
    )

def movie_genre(request, genre_name):
    genres = Genre.objects.all()

    m_genre = Genre.objects.get(name=genre_name)

    movies = Movie.objects.filter(genre=m_genre)

    rating = request.GET.get('rating', '')
    if rating:
        movies = movies.filter(rating__gt=rating)

    an = request.GET.get('an', '')
    if an:
        an = int(an)
        d = date(an, 1, 1)
        movies = movies.filter(released__gt=d)

    return render(
        request, template_name='home.html',
        context={'movies': movies, 'genres': genres}
    )
