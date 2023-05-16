from django.db import models

# Create your models here.
class Hello(models.Model): # there'll be a table call Hello in db
    text = models.CharField(max_length=200) 

class Person(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False, db_index=True) 
    age = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    number = models.IntegerField(null=False, blank=True)
    street_name = models.CharField(max_length=500, null=True, blank=True)
    resident = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)