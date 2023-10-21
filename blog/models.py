from django.db import models
from accounts.models import CustomUser
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    description = models.TextField()
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Response(models.Model):
    response = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return f'{self.author.username} | {self.date}'
    
class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    responses = models.ManyToManyField(Response, blank=True)
    
    def __str__(self):
        return f'{self.author.username} | {self.date}'
