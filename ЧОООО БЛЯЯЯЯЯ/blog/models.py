from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from config import settings
# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,unique=True,blank=True,null=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    job = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=15,unique=True,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    website = models.URLField(blank=True,null=True)
    github = models.CharField(max_length=55,blank=True,null=True)
    instagram = models.CharField(max_length=55,blank=True,null=True)
    facebook = models.CharField(max_length=55,blank=True,null=True)
    photo = models.ImageField(upload_to='articles/', blank=True)

class Category(models.Model):
    title = models.CharField(max_length=155,unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='articles/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser,null=True,blank=True,default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_photo(self):
        try:
            return self.photo.url
        except:
            return "https://peoplevine.blob.core.windows.net/media/72/e86f3854-ebcf-4025-ae66-220b51f77ec2/image_not_available.png"

    def get_absolute_url(self):
        return reverse('article',kwargs={'pk':self.pk})

class Comment(models.Model):
    title = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
