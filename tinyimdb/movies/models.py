from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    script = models.TextField()
    actors = models.CharField(max_length=400)
    director = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    budget = models.CharField(max_length=4)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title