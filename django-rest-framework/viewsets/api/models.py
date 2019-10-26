from django.db import models

 
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
 
    def __str__(self):
       return "{name}".format(name=self.name)
