from django.db import models

# Create your models here.


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, default="")
    email = models.CharField(max_length=255, unique=True, default="")
    country = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="", unique=True)
    blocked = models.BooleanField(default=False)


class Talent(User):
    socialNetWork = models.CharField(max_length=255, default="")
    nickname = models.CharField(max_length=255, default="")
    followers = models.IntegerField(default=0)
    description = models.CharField(max_length=255, default="")
    rating = models.FloatField(default=0)






