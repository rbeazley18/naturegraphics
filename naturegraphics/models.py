from unicodedata import category
from django.db import models

class Portfolio(models.Model):
    order = models.IntegerField(default='1')
    title = models.CharField(max_length=255, blank=False, null=True, default='Title')
    description = models.TextField(blank=True)
    portfolio_image = models.ImageField(null=True, blank=False, upload_to='images/portfolio')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Our Projects'

class Gallery(models.Model):
    order = models.IntegerField(default='1')
    alt_tag = models.CharField(max_length=255, blank=False, null=True, default='Alt Tag')
    gallery_image = models.ImageField(null=True, blank=False, upload_to='images/gallery')

    def __str__(self):
        return self.alt_tag

    class Meta:
        verbose_name_plural = 'Gallery'

class Project1(models.Model):
    order = models.IntegerField(default='1')
    category = models.CharField(max_length=255, blank=False, null=True, default='Category')
    alt_tag = models.CharField(max_length=255, blank=True)
    project_image = models.ImageField(null=True, blank=False, upload_to='images/project1')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Cultural History'

class Project2(models.Model):
    order = models.IntegerField(default='1')
    category = models.CharField(max_length=255, blank=False, null=True, default='Category')
    alt_tag = models.CharField(max_length=255, blank=True)
    project_image = models.ImageField(null=True, blank=False, upload_to='images/project2')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Natural History'

class Project3(models.Model):
    order = models.IntegerField(default='1')
    category = models.CharField(max_length=255, blank=False, null=True, default='Category')
    alt_tag = models.CharField(max_length=255, blank=True)
    project_image = models.ImageField(null=True, blank=False, upload_to='images/project3')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Park Information'

class Project4(models.Model):
    order = models.IntegerField(default='1')
    category = models.CharField(max_length=255, blank=False, null=True, default='Category')
    alt_tag = models.CharField(max_length=255, blank=True)
    project_image = models.ImageField(null=True, blank=False, upload_to='images/project4')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Resource Management'


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email