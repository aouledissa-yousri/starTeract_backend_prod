from ..serializers import TalentSerializer
from ..classes.UserClass import UserClass
from ..classes.ClassificationClass import ClassificationClass

class TalentClass(UserClass):
    __socialNetwork = ""
    __nickname = ""
    __followers = 0
    __description = ""
    __rating = 0

    def __init__(self, request=None):
        if request == None:
            pass 
        else:
            super().__init__(request)
            self.__socialNetwork = request.get("rulingSocialNetwork")
            self.__nickname = request.get("nickname")
            self.__followers = request.get("followers")
            self.__description = request.get("description")
    
    def getData(self):
        data = super().getData()
        data["socialNetwork"] = self.__socialNetwork
        data["nickname"] = self.__nickname
        data["followers"] = self.__followers
        data["description"] = self.__description
        data["rating"] = self.__rating
        data["blocked"] = True
        return data
    
    def signUp(self, request):
        self.__init__(request)
        serializer = TalentSerializer(data=self.getData())
        if serializer.is_valid():
            serializer.save()
            ClassificationClass.saveClassifications(self, request)
        return serializer.is_valid()
    
        