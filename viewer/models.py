from django.db.models import (CharField, Model, ForeignKey,
    DO_NOTHING, IntegerField, DateField,
    TextField, DateTimeField, SlugField)

from django.utils.text import slugify


# Create your models here.
class Genre(Model):
    name = CharField(max_length=128)

    # functie apelata implicit de django atunci cand afiseaza un obiect din baza de date
    # returneaza numele cu care va fi afisat obiectul in interfata de admin
    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=128)

    # ForeignKey face referire la un obiect din tabelul Genre
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()

    # Camp care contine o data (zi/luna/an)
    released = DateField()
    description = TextField()

    # Camp care contine o data si ora (zi/luna/an ora/minut/secunda)
    # auto_now_add adauga ora si data la care s-a creat obiectul automat
    created = DateTimeField(auto_now_add=True)

    # Slug se refera la numele obiectul in format corect pentru URL
    # ex: Nume: The Good Place -> Slug: the-good-place
    # unique=True -> nu putem avea doua obiecte cu acelasi slug
    # editable=False -> nu putem edita noi acest camp
    slug = SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title