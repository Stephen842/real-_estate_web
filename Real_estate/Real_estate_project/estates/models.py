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