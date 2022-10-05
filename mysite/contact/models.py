from ckeditor.fields import RichTextField
from django.db import models


class Contact(models.Model):
    """ feedback model class """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    time_create = models.DateTimeField("time create", auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class About(models.Model):
    """ about us page model class """
    image = models.ImageField(upload_to="about/")
    message = RichTextField()

