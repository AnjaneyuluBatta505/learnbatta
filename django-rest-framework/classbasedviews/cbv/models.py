from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    released_on = models.DateField()
    genre = models.CharField(max_length=250)
    director = models.CharField(max_length=250)


    def __str__(self):
        return self.title
