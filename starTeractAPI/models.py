from django.db import models
from django.core.validators import MaxValueValidator

BASE = "http://127.0.0.1:8000/media/"


# Create your models here.
def uploadPathVideo(instance, fileName):
    return "/".join(["videos", str(instance.title), fileName])

def uploadPathImage(instance, fileName):
    return "/".join(["images", str(instance.title), fileName])

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, default="", unique=True)
    email = models.CharField(max_length=255, default="", unique=True)
    country = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="", unique=True)
    image = models.CharField(max_length=3000, default="images/default/user.jfif",blank=True, null=True)
    blocked = models.BooleanField(default=False)
    tries = models.IntegerField(default=3, validators = [ MaxValueValidator(3)])


class Talent(User):
    socialNetwork = models.CharField(max_length=255, default="")
    nickname = models.CharField(max_length=255, default="")
    followers = models.BigIntegerField(default=0)
    description = models.CharField(max_length=255, default="")
    rating = models.FloatField(default=0)
    verified = models.BooleanField(default=True)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos1")
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="videos2")
    title = models.CharField(max_length=255, default="")
    video = models.FileField(upload_to=uploadPathVideo, blank=True, null=True, max_length=255)
    #video = models.ImageField(upload_to=uploadPath, blank=True, null=True, max_length=255)

    

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
    TYPES = (
        ("video", "video"),
        ("payment", "payment")
    )
    
    #who requests the task
    emitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emitter1")
    #who does the task
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver1")
    task = models.CharField(max_length=255, default="")
    type = models.CharField(max_length=255, default="payment", choices=TYPES)

class Image(models.Model):
    title = models.CharField(max_length=255, default="", unique=True)
    image = models.FileField(upload_to=uploadPathImage, blank=True, null=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user7", unique=True)








