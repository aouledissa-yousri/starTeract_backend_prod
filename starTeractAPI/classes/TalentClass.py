from ..serializers import TalentSerializer
from ..classes.UserClass import UserClass
from ..classes.CategoryClass import CategoryClass
from ..classes.ClassificationClass import ClassificationClass
from ..models import Talent, User, Category, Classification, Review
from django.db.models import Q
from ..models import BASE




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
    
    @staticmethod 
    def getTalent(i):
        talent = Talent.objects.get(id=i)
        classification = Classification.objects.filter(talent_id=talent.id)
        categories = []
        for i in range(0, len(classification)):
            categories.append(CategoryClass.getCategory(classification[i].category_id))
        return {
            "id": talent.id,
            "name": talent.name,
            "email": talent.email,
            "country": talent.country,
            "password": "",
            "socialNetwork": talent.socialNetwork,
            "nickname": talent.nickname,
            "followers": talent.followers,
            "description": talent.description,
            "rating": talent.rating,
            "image" : BASE + str(talent.image),
            "categories": categories
        }
    
    @staticmethod
    def getTalents(id):
        talents = []
        for talent in Talent.objects.all():
            try:
                if id != talent.id: 
                    talents.append(TalentClass.getTalent(talent.id))
            except:
                continue
        return talents
    
    @staticmethod
    def getTalentByName(talentName):
        talent = Talent.objects.get(name=talentName)
        classification = Classification.objects.filter(talent_id=talent.id)
        categories = []
        for i in range(0, len(classification)):
            categories.append(CategoryClass.getCategory(classification[i].category_id))
        return {
            "id": talent.id,
            "name": talent.name,
            "email": talent.email,
            "country": talent.country,
            "password": "",
            "socialNetwork": talent.socialNetwork,
            "nickname": talent.nickname,
            "followers": talent.followers,
            "description": talent.description,
            "rating": talent.rating,
            "image" : BASE + str(talent.image),
            "categories": categories,
            "reviews": TalentClass.getReviews(talent.id)
        }
    

    @staticmethod
    def getReviews(id):
        records = Review.objects.filter(talent_id=id)
        reviews = {
            "reviewNum": records.count(),
            "content": []
        }

        for i in range(0,len(records)):
            reviews["content"].append({
                "comment": records[i].comment,
                "rating": records[i].rating,
                "user": records[i].user_id,
                "username": User.objects.get(id=records[i].user_id).name,
                "userImage": BASE + str( User.objects.get(id=records[i].user_id).image)
            })
        return reviews

    
        