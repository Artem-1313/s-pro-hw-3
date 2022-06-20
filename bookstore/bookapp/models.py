from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

year = [(i, i) for i in range(1800, 2022)]

class Author(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    released_year = models.IntegerField(max_length=100, choices=year, default=2022)
    pages = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}"


