from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tags(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField("URL", max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField("URL", max_length=255, unique=True, db_index=True)
    content = RichTextField()
    image = models.ImageField(upload_to="photos/%Y/%m/%d")
    tag = models.ForeignKey('Tags', on_delete=models.SET_NULL, null=True)
    time_create = models.DateTimeField("time create", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def get_comments(self):
        return self.comment.all().only('message', 'name', 'time_create','post')


class Comment(models.Model):
    message = models.TextField(max_length=1000)
    website = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    time_create = models.DateTimeField("time create", auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    icon = models.ImageField(upload_to="social/")


class UserEmails(models.Model):
    email = models.EmailField()