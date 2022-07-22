import email
from pydoc import describe
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.db import models

# Create your models here.
 
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Rate(models.Model):
    rate = models.IntegerField(default=0)
    comment = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.rate+self.comment