from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    genre = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.genre
    