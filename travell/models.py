from django.db import models


# Create your models here.


class Features(models.Model):

    feature = models.TextField(max_length=30)


class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    comment = models.TextField()
    features = models.ManyToManyField(Features)
