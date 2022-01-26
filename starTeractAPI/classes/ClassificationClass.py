from ..serializers import ClassificationSerializer

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
        


