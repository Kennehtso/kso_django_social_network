from django.db import models

# Create your models here.
class Hello(models.Model): # there'll be a table call Hello in db
    text = models.CharField(max_length=200) 
