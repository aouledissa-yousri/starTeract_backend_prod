from ..models import User
from ..serializers import UserSerializer
from ..classes.Credentials import Credentials
import random 
import string 



class UserClass:
    __id = 0
    __name = ""
    __email = ""
    __country = ""
    __password = ""
    __phone = ""

    def __init__(self, request=None):
        if request == None :
            pass
        else:
            self.__id = User.objects.all().count() + 1
            self.__name = request.POST.get("name")
            self.__email = request.POST.get("email")
            self.__country = request.POST.get("country")
            self.__password = Credentials.hash(request.POST.get("password"))
            self.__phone = request.POST.get("phone")
   
    def getData(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "email": self.__email,
            "country": self.__country,
            "password": self.__password,
            "phone": self.__phone
        }
    
    def signUp(self, request):
        self.__init__(request)
        serializer = UserSerializer(data=self.getData())
        if serializer.is_valid():
            serializer.save()
        return serializer.is_valid()
    
    def login(self, request):
        credentials = Credentials(request)
        target = (User.objects.filter(name=credentials.getCredentials()["name"]) | User.objects.filter(email=credentials.getCredentials()["email"])) & User.objects.filter(password=credentials.getCredentials()["password"])
        if target.count() != 0:
            return True
        return False

    

    '''@staticmethod
    def generateToken():
        chars = string.printable
        return ''.join(random.choice(chars) for i in range(random.randint(32,150)))'''
    


    

