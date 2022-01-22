from ..serializers import TalentSerializer
from ..classes.UserClass import UserClass

class TalentClass(UserClass):
    __socialNetwork = ""
    __nickname = ""
    __followers = 0
    __description = ""
    __rating = 0

    def __init__(self, request=None):
        super().__init__(request)
        if request == None:
            pass 
        else:
            self.__socialNetwork = request.POST.get("socialNetwork")
            self.__nickname = request.POST.get("nickname")
            self.__followers = request.POST.get("followers")
            self.__rating = request.POST.get("description")
    
    def getData(self):
        data = super().getData()
        data["socialNetwork"] = self.__socialNetwork
        data["nickname"] = self.__nickname
        data["followers"] = self.__followers
        data["description"] = self.__description
        data["rating"] = self.__rating
        return data
    
    def signUp(self, request):
        self.__init__(request)
        serializer = TalentSerializer(data=self.getData())
        if serializer.is_valid():
            serializer.save()
        return serializer.is_valid()
    
        