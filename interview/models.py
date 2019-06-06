from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Category(models.Model):
    category_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.category_name

class Question(models.Model):
    question = models.CharField(max_length = 500)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    answer = models.CharField(max_length = 500)

    def __str__(self):
        return self.question

class Note(models.Model):
    item = models.CharField(max_length = 500)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.item
