from tabnanny import verbose
from turtle import title
from unicodedata import category
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=255)
    # category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')



class Project(models.Model):
    order = models.IntegerField(default='1')
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    # title = description = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    project_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.description


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email