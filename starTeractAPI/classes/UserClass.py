from ..models import User
from ..serializers import UserSerializer, CredentialsSerializer
from ..classes.Credentials import Credentials
from django.db.models import Q


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
        serializer = CredentialsSerializer(data=credentials.getCredentials())
        if serializer.is_valid():
            target = User.objects.filter(name=request.POST.get("username"))
            if target.count() != 0:
                return True
        return False
    


    

