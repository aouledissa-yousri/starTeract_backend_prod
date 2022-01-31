from ..serializers import ServiceSerializer
from ..classes.NotificationClass import NotificationClass

class ServiceClass:
    user = 0
    talent = 0 
    occasion = ""
    description = ""
    type = ""

    def __init__(self, request = None):
        if request == None: 
            pass
        else: 
            self.user = request.get("service").get("user")
            self.talent = request.get("service").get("talent")
            self.occasion = request.get("service").get("occasion")
            self.description = request.get("service").get("description")
            self.type = request.get("service").get("type")
    

    def getData(self):
        return {
            "description": self.description,
            "occasion": self.occasion,
            "type": self.type,
            "user": self.user,
            "talent": self.talent
        }
    
    def saveService(self, request):
        self.__init__(request)
        serializer = ServiceSerializer(data=self.getData())
        notification = NotificationClass(request)
        if notification.push():
            if serializer.is_valid():
                serializer.save()
        return serializer.is_valid()