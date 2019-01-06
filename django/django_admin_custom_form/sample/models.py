from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)
