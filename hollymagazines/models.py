from django.db import models
from django.utils.text import slugify

# Create your models here.
from django.db.models import CharField, Model, ForeignKey, DO_NOTHING, IntegerField, DateField, TextField, \
    DateTimeField, SlugField


class Publicatie(Model):

    class Meta:
        verbose_name_plural = "Publicatie"
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Revista(Model):

    class Meta:
        verbose_name_plural = "Revista"

    title = CharField(max_length=128)
    publicatie = ForeignKey(Publicatie, on_delete=DO_NOTHING)
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
    slug = SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
