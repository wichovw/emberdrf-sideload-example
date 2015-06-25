from django.db import models

# Create your models here.

class BigThing(models.Model):
    name = models.CharField(max_length=100)
    favorite = models.OneToOneField('ChildThing', related_name='favorite_of')
    
class ChildThing(models.Model):
    father = models.ForeignKey(BigThing)
    name = models.CharField(max_length=100)