from django.db import models

class ContacIfo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
       return self.first_name