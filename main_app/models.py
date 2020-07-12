from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    illustrated = models.CharField(max_length = 100)
    age = models.CharField(max_length = 100)

    def __str__(self):
        return self.title