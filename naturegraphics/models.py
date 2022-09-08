from tabnanny import verbose
from unicodedata import category
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)
    category_description = models.CharField(max_length=255)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Project(models.Model):
    order = models.IntegerField(default='1')
    category = models.ForeignKey(Category, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)
    description = models.CharField(max_length=255, blank=True)
    project_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email