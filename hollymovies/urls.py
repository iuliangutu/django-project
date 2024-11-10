"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import home, film, genres
from viewer.views import home, movie_detail, movie_genre

urlpatterns = [
    path('admin/', admin.site.urls),

    # Parametrii cu regular expressions
    # Regular expressions
    # path('hello/<s>/<other_s>', hello)

    # Parametrii cu URL Encoding
    # Url encoding
    path('', home, name='home'),

    path('film/<slug:my_slug>', film, name='film'),

    path("genre/<str:name>/", genres, name="genre"),

    path('movie/<slug:slug>', movie_detail, name='movie_detail'),
    path('gen/<str:genre_name>', movie_genre, name='movie_genre')
]


# python manage.py dumpdata viewer --output fixtures.json