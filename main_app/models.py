from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    illustrated = models.CharField(max_length = 100)
    age = models.CharField(max_length = 100)
    likes = models.ManyToManyField(User, related_name='book_posts')
    bookImage = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={ 'book_id': self.id })

    def total_likes(self):
        return self.likes.count()