from django.db import models
from datetime import datetime
import re
import bcrypt
from ReadApp.models import User

class User_manager(models.Manager):
    def book_validator(self, postData):
        errors = {}

        #title validation
        if len(postData['title'])< 2:
            errors['title'] = "Title must be at least 2 characters."
        title = Book.objects.filter(title=postData['title'])
        if len(title) >0:
            errors['title'] = "This title already exists."  

        return errors  


class Author(models.Model):
    name = models.CharField(max_length=45)
    #books = related name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
    #review = related name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_manager()

class Review(models.Model):
    words = models.CharField(max_length=255)
    stars = models.CharField(max_length=1)
    user = models.ForeignKey(User, related_name="review", on_delete = models.CASCADE)
    book = models.ForeignKey(Book, related_name='review', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_manager()


