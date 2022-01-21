from django.db import models
import hashlib
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.IntegerField()


    def getData(self, request):
        return {
            "id": User.objects.all().count() + 1,
            "name": request.POST.get("name"),
            "email" : request.POST.get("email"),
            "country" : request.POST.get("country"),
            "password" : self.__hash(request.POST.get("password")),
            "phone" : int(request.POST.get("phone"))
        }
    
    def __hash(self, password):
        result = hashlib.sha256(password.encode())
        return result.hexdigest()


class Talent(User):
    rulingSocialNetwork = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    followers = models.IntegerField(default=0)

    def getData(self, request):
        data = super().getData(request)
        data["rulingSocialNetwork"] = request.POST.get("rulingSocialNetwork")
        data["nickname"] = request.POST.get("nickname")
        data["followers"] = int(request.POST.get("followers"))
        return data

