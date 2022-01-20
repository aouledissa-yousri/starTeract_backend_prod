from django.db import models
import hashlib

# Create your models here.
from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.IntegerField()


    def getData(self, request):
        self.id = User.objects.all().count() + 1
        self.name = request.POST.get("name")
        self.email = request.POST.get("email")
        self.country = request.POST.get("country")
        self.password = self.__hash(request.POST.get("password"))
        self.phone = request.POST.get("phone")
    
    def __hash(self, password):
        result = hashlib.sha256(password.encode())
        return result.hexdigest()


class Talent(User):
    rulingSocialNetwork = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    followers = models.IntegerField(default=0)

    def getData(self, request):
        super().getData(request)
        self.rulingSocialNetwork = request.POST.get("rulingSocialNetwork")
        self.nickname = request.POST.get("nickname")
        self.followers = request.POST.get("followers")

