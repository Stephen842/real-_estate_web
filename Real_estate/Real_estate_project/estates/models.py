from django.db import models
from PIL import Image

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 300)
    body = models.TextField()
    image = models.ImageField(upload_to = 'media/', null = True, blank = True)
    image_1 = models.ImageField(upload_to='media/', null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    categories = models.ManyToManyField('Category', related_name = 'posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length = 80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"


class Contact(models.Model):
    name = models.CharField(max_length = 250, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length = 255)
    message = models.TextField()

    def __str__(self):
        return self.email
    
class Newsletter(models.Model):
    email = models.EmailField(blank = True)

    def __str__(self):
        if self.email:
            return self.email
        else:
            return 'No email provided'
        
class Property(models.Model):
    title = models.CharField(max_length = 300)
    description = models.TextField()
    image = models.ImageField(upload_to = 'media/', null = True, blank = True)
    image_1 = models.ImageField(upload_to='media/', null = True, blank = True)
    image_2 = models.ImageField(upload_to='media/', null = True, blank = True)
    price = models.CharField(max_length = 300)
    location = models.CharField(max_length = 300)
    size = models.CharField(max_length = 300)
    bed = models.IntegerField(blank=False)
    toilet = models.IntegerField(blank=False)
    bathroom = models.IntegerField(blank=False)
    parking = models.IntegerField(blank=False)
    date_created = models.DateTimeField(auto_now_add = True)
    categories = models.ManyToManyField('Category', related_name = 'property')
    
    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title

class PropertyContact(models.Model):
    name = models.CharField(
        max_length = 250,
        blank=False,
        )
    phone = models.CharField(
        max_length = 30,
        blank=False,
        )
    message = models.TextField()

    def __str__(self):
        return self.name