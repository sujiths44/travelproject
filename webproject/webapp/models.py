from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic5')
    desc=models.TextField()
    def __str__(self):
        return self.name

class Team(models.Model):
    person=models.CharField(max_length=250)
    picture=models.ImageField(upload_to='pic5')
    descrip=models.TextField()

