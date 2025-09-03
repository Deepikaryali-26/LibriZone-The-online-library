from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Education', 'Education'),
        ('Fiction', 'Fiction'),
        ('Thriller', 'Thriller'),
        ('Mythology', 'Mythology'),
        ('Comics','Comics'),

    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    pdf_file = models.FileField(upload_to='ebook/')
    cover_image = models.ImageField(upload_to='images', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

        
def __str__(self):
        return self.title

