from ..serializers import TalentSerializer
from ..classes.UserClass import UserClass
from ..classes.ClassificationClass import ClassificationClass
from ..models import Talent, User
from django.db.models import Q



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
        return data
    
    def signUp(self, request):
        self.__init__(request)
        serializer = TalentSerializer(data=self.getData())
        if serializer.is_valid():
            serializer.save()
            ClassificationClass.saveClassifications(self, request)
        return serializer.is_valid()
    
    def login(self, request):
        if TalentClass.checkIfTalent(request).get("message"):
            if Talent.objects.get(user_ptr_id=TalentClass.checkIfTalent(request)["id"]).verified:
                return super().login(request)
            return {"message": "your account is not verified yet"}
        else:
            return super().login(request)

        
    
    @staticmethod
    def checkIfTalent(request):
        try:
            result = Talent.objects.get(user_ptr_id = User.objects.get(Q(name=request.get("name")) | Q(email=request.get("email"))).id).user_ptr_id
            return {
                "message": True,
                "id" : result
            }
        except:
            return {"message" : False}

    
        