from ..serializers import ServiceSerializer
from ..classes.NotificationClass import NotificationClass
from ..models import Service, User

class ServiceClass:
    id = 0
    user = 0
    talent = 0 
    occasion = ""
    description = ""
    type = ""

    def __init__(self, request=None, service=None):
        if request == None and service == None: 
            pass
        elif request != None: 
            self.id = Service.objects.all().count() + 1
            self.user = request.get("service").get("user")
            self.talent = request.get("service").get("talent")
            self.occasion = request.get("service").get("occasion")
            self.description = request.get("service").get("description")
            self.type = request.get("service").get("type")
        elif service != None: 
            self.id = service.id
            self.user = service.user_id
            self.talent = service.talent_id
            self.occasion = service.occasion
            self.description = service.description
            self.type = service.type
    

    def getData(self):
        return {
            "id": self.id,
            "description": self.description,
            "occasion": self.occasion,
            "type": self.type,
            "user": self.user,
            "talent": self.talent
        }
    
    def saveService(self, request):
        self.__init__(request)
        serializer = ServiceSerializer(data=self.getData())
        notification = NotificationClass(request, None)
        if notification.push():
            if serializer.is_valid():
                serializer.save()
        return serializer.is_valid()
    
    @staticmethod
    def getServices(id):
        try: 
            services = Service.objects.filter(talent_id=id)   
            tasks = []
            for service in services:
                task = ServiceClass(None,service)  
                tasks.append({
                    "service": task.getData(),
                    "user": {
                        "name": User.objects.get(id=service.user_id).name,
                        "image": User.objects.get(id=service.user_id).image
                    }
                })
            return tasks
        except: 
            return None
    
    @staticmethod 
    def deleteService(request,id_):
        Service.objects.filter(id=id_).delete()
        notification = NotificationClass(request)
        notification.push()
    
    @staticmethod 
    def updateService(idf):
        Service.objects.filter(id=idf).update(state="accepted")
    
    @staticmethod 
    def completeService(idf): 
        Service.objects.filter(id=idf).delete()
