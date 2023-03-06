from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.



class PublishedManager(models.Manager):
 def get_queryset(self):
    return super().get_queryset()\
                            .filter(status=Post.Status.PUBLISHED)
class Articulo(models.Model):
    name= models.CharField(max_length=50)
    stock= models.IntegerField(blank=True,null=True)
    pvp=models.DecimalField(max_digits=8, decimal_places=2)
    imagen= models.ImageField(upload_to='articulos/')
class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    name = models.CharField(max_length=50)
    pvp = models.IntegerField(blank=True,null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    #objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
         ordering = ['-publish']
         indexes = [
            models.Index(fields=['-publish']),
         ]
    def __str__(self):
        return self.name