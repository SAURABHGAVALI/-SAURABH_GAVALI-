from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=CustomManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

class Yoga(models.Model):
    Cname=models.CharField(max_length=64)
    age=models.IntegerField()
    Email=models.EmailField()
    MobileNo=models.IntegerField()
    Gender=models.CharField(max_length=64)


class GYM(models.Model):
    TraineeName=models.CharField(max_length=64)
    age=models.IntegerField()
    Email=models.EmailField()
    MobileNo=models.IntegerField()
    Gender=models.CharField(max_length=64)
    City_Name=models.CharField(max_length=64)



class PRANIC(models.Model):
    Name=models.CharField(max_length=64)
    age=models.IntegerField()
    Email=models.EmailField()
    MobileNo=models.IntegerField()
    Gender=models.CharField(max_length=64)
    City_Name=models.CharField(max_length=64)



class ADVENTURE(models.Model):
    Name=models.CharField(max_length=64)
    age=models.IntegerField()
    Email=models.EmailField()
    MobileNo=models.IntegerField()
    Gender=models.CharField(max_length=64)
    City_Name=models.CharField(max_length=64)

class MEDITATION(models.Model):
    Name=models.CharField(max_length=64)
    age=models.IntegerField()
    Email=models.EmailField()
    MobileNo=models.IntegerField()
    Gender=models.CharField(max_length=64)
    City_Name=models.CharField(max_length=64)
