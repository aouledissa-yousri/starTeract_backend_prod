from ..models import User
from ..serializers import UserSerializer
from ..classes.Credentials import Credentials
from django.db.models import Q
import jwt
import time
from threading import Thread

class UserClass:
    __id = 0
    __name = ""
    __email = ""
    __country = ""
    __password = ""
    __phone = ""
    __blocked = False

    def __init__(self, request=None):
        if request == None :
            pass
        else:
            self.__id = User.objects.all().count() + 1
            self.__name = request.get("name")
            self.__email = request.get("email")
            self.__password = request.get("password")
            self.__country = request.get("country")
            self.__phone = request.get("phone")
            self.__blocked = False
   
    def getData(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "email": self.__email,
            "country": self.__country,
            "password": self.__password,
            "phone": self.__phone,
            "blocked": self.__blocked
        }
    
    def signUp(self, request):
        self.__init__(request)
        serializer = UserSerializer(data=self.getData())
        if serializer.is_valid():
            serializer.save()
        return serializer.is_valid()
    
    def login(self, request):
        try:
            credentials = Credentials(request)
            target = User.objects.get((Q(name=credentials.getCredentials()["name"]) | Q(email=credentials.getCredentials()["email"])))
            if target:
                if target.password == credentials.getCredentials()["password"] and target.blocked == False:
                    return {
                        "message": "success",
                        "id": target.id,
                        "name": target.name,
                        "token" : UserClass.generateToken({
                            "name": credentials.getCredentials()["name"],
                            "id": target.id
                        })    
                    }
                User.objects.filter(id = target.id).update(tries= target.tries - 1)
                if target.tries < 1:
                    User.objects.filter(id = target.id).update(blocked= True)
                    Thread(target= self.__restart, args=(target.id,)).start()
                    return {"message": "your account is temporarily blocked please try again later!"}
                return {"message": "password is wrong"}
        except:
            return {"message": "user not found"}

    def __restart(self, id):
        if self.__blocked == False:
            self.__blocked = True
            time.sleep(18000)
            User.objects.filter(id = id).update(tries= 3)
            User.objects.filter(id = id).update(blocked= False)
            self.__blocked = False


    @staticmethod
    def generateToken(payload):
        return jwt.encode(payload, "django-insecure-olcf)=r)pwgqpnc3jcvob#abk*#k29mw!zp=2taufgvfm&)-v0", algorithm="HS256")
    
    @staticmethod
    def getUserData(request):
        user = User.objects.get(id = request.get("id"))
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "country": user.country,
            "phone": user.phone,
            "image": user.image
        }
     

    

    


    

