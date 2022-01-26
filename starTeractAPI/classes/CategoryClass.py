from ..models import Category
from ..serializers import CategorySerializer

class CategoryClass:
    __id = 0
    __name = ""

    def __init__(self, name, id=None):
        if id == None:
            self.__id = Category.objects.all().count() + 1
            self.__name = name
        else:
            self.__id = id
            self.__name = name
    
    def getData(self):
        return {
            "id": self.__id,
            "name": self.__name
        }
    
    def save(self):
        serializer = CategorySerializer(data=self.getData())
        if serializer.is_valid():
            serializer.save()
    
    @staticmethod
    def getCategories():
        data = []
        for category in Category.objects.all():
            data.append(CategoryClass(category.name, category.id).getData())
        return data

        
        

