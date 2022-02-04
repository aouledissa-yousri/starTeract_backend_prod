from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, default="", unique=True)
    email = models.CharField(max_length=255, default="", unique=True)
    country = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="", unique=True)
    image = models.CharField(max_length=3000, default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Z5BlhFYs_ga1fZnBWkcKjQHaHz%26pid%3DApi&f=1")
    blocked = models.BooleanField(default=False)
    tries = models.IntegerField(default=3, validators = [ MaxValueValidator(3)])


class Talent(User):
    socialNetwork = models.CharField(max_length=255, default="")
    nickname = models.CharField(max_length=255, default="")
    followers = models.BigIntegerField(default=0)
    description = models.CharField(max_length=255, default="")
    rating = models.FloatField(default=0)
    verified = models.BooleanField(default=False)


class Notification(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=255, default="")
    checked = models.BooleanField(default=False)
    emitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emitter")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    content = models.CharField(max_length=255, default="")
    
class Service(models.Model):
    TYPES = (
        ("Advertisement", "Advertisement"),
        ("Personal Video", "Personal Video")
    )

    TYPES2 = (
        ("waiting", "waiting"),
        ("accepted", "accepted")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="talent")
    description = models.CharField(max_length=255, default="")
    occasion = models.CharField(max_length=255, default="")
    type = models.CharField(max_length=255, default="", choices=TYPES)
    state = models.CharField(max_length=255, default="waiting", choices=TYPES2)


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="talent2")
    title = models.CharField(max_length=255, default="")
    source = models.CharField(max_length=255, default="")

class Category(models.Model):
    name = models.CharField(max_length=255, default="")

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user3", unique=True)
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="talent3")
    comment = models.CharField(max_length=255, default="")
    rating = models.FloatField(default=0)

class Classification(models.Model):
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="talent4")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")

    class Meta:
        unique_together = ["talent", "category"]

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user5")
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="talent5")
    task = models.CharField(max_length=255, default="")








