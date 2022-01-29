from ..serializers import ClassificationSerializer
from ..models import Classification

class ClassificationClass:
       
    @staticmethod
    def getClassifications(talent, request):
        classifications = []
        categories = request.get("categories")
        for category in categories:
            classifications.append({
                "category": category["id"], 
                "talent": talent.getData()["id"]
            })

        return classifications
    

    @staticmethod
    def saveClassifications(talent, request):
        classifications = ClassificationClass.getClassifications(talent, request)
        for classification in classifications:
            serializer = ClassificationSerializer(data=classification)
            if serializer.is_valid():
                serializer.save()
    
    @staticmethod
    def getSavedClassifications():
        classifications = []
        for classification in Classification.objects.all():
            classifications.append({
                "idTalent": classification.talent_id,
                "idCategory": classification.category_id
            })
        return classifications
        


