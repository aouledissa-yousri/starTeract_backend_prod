from django.db import models

# Create your models here.


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, default="", unique=True)
    email = models.CharField(max_length=255, default="", unique=True)
    country = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="", unique=True)
    blokced = models.BooleanField(default=False)


class Talent(User):
    socialNetwork = models.CharField(max_length=255, default="")
    nickname = models.CharField(max_length=255, default="")
    followers = models.BigIntegerField(default=0)
    description = models.CharField(max_length=255, default="")
    rating = models.FloatField(default=0)

class Notification(models.Model):
    description = models.CharField(max_length=255, default="")
    checked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    content = models.CharField(max_length=255, default="")
    
class Service(models.Model):
    TYPES = (
        ("Advertisement", "Advertisement"),
        ("Personal Video", "Personal Video")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="talent")
    description = models.CharField(max_length=255, default="")
    occasion = models.CharField(max_length=255, default="")
    type = models.CharField(max_length=255, default="", choices=TYPES)


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







