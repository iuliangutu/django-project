from django.shortcuts import render
from datetime import date

# Create your views here.
from django.http import HttpResponse

from viewer.models import Movie, Genre
from django.urls import resolve


# Url parameters cu regular expressions
# def hello(request, s, other_s):
#     return HttpResponse(f'Hello, {s} and {other_s} World!')

# URL Encoding
# def hello(request):
    # print(request.GET)
    # s = request.GET.get('s', '')
    # other_s = request.GET.get('other_s', '')
    # return HttpResponse(f'Hello {s} and {other_s} World!')

# Exemple de queries
# def hello(request):
    # sql WHERE -> .filter()
    # movie1 = Movie.objects.filter(rating=8)

    # Filemele unde genre-ul are numele SciFi
    # genre = Genre.objects.get(name='SciFi')
    # movie2 = Movie.objects.filter(genre=genre)

    # Filmele cu rating mai mare de 8
    # movie3 = Genre.objects.filter(rating__gt=8)

    # .filter() inlantuite
    # movie4 = Movie.objects.filter(title_icontains='godfather').filter(rating=10)

    # cate obiecte sunt in query
    # movie_count = Movie.obejcts.all().count()

    # Varianta 1 de creat un obiect
    # Genre.objects.create(name='Horror')

    # sau varianta 2
    # g = Genre.objects.create(name='Horror')
    # g.save()

    # return HttpResponse('<h1>Filmele mele</h1>')


def home(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    rating = request.GET.get("rating", "")
    print(rating)
    rating = request.GET.get('rating', '')
    if rating:
        movies = movies.filter(rating__gt=rating)

    movies = Movie.objects.filter(rating__gt=3)
    an = request.GET.get('an', '')
    if an:
        an = int(an)
        d = date(an, 1, 1)
        movies = movies.filter(released__gt=d)

    return render(
        request, template_name = 'home.html',
        context = {'filme': movies,
                    'genres': genres}
    )
        request, template_name='home.html',
        context={'movies': movies, 'genres': genres})

def film(request, my_slug):
    movie = Movie.objects.get(slug=my_slug)
    print(movie)
def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)

    return render(
        request, template_name='film.html',
        context={'film': movie}
        request, template_name='movie.html',
        context={'movie': movie}
    )

def genres(request, name):

    movies = Movie.objects.all()
def movie_genre(request, genre_name):
    genres = Genre.objects.all()

    # Filmele unde genre-ul are numele comedie
    genre = Genre.objects.get(name=name)
    print(genre)
    m_genre = Genre.objects.get(name=genre_name)

    movies_genre = Movie.objects.filter(genre=genre)
    print(movies_genre)
    movies = Movie.objects.filter(genre=m_genre)

    rating = request.GET.get("rating", "")
    print(rating)

    if rating != "":
        movies = movies_genre.filter(rating__gt=rating)
    rating = request.GET.get('rating', '')
    if rating:
        movies = movies.filter(rating__gt=rating)

    an = request.GET.get('an', '')
    if an:
        an = int(an)
        d = date(an, 1, 1)
        movies = movies.filter(released__gt=d)

    return render(
        request, template_name="home.html",
        context={"genres": genres,
                 "filme": movies,
                 }
        request, template_name='home.html',
        context={'movies': movies, 'genres': genres}
    )








