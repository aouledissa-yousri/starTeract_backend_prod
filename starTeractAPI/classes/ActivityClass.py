from ..serializers import ActivitySerializer
from ..classes.NotificationClass import NotificationClass
from ..models import Activity, User
from ..models import BASE

class ActivityClass: 
    id = 0
    emitter = 0
    receiver = 0
    task = ""
    type = ""


    def __init__(self, request=None):
        if request == None:
            pass
        elif request != None:
            self.id = Activity.objects.all().count() + 1
            self.emitter = request.get("activity").get("emitter")
            self.receiver = request.get("activity").get("receiver")
            self.task = request.get("activity").get("task")
            self.type = request.get("activity").get("type")
    

    def getData(self): 
        return {
            "id": self.id,
            "emitter": self.emitter,
            "receiver": self.receiver,
            "task": self.task,
            "type": self.type
        }
    
    def saveActivity(self, request):
        self.__init__(request)
        notification = NotificationClass(request)
        serializer = ActivitySerializer(data=self.getData())
        if notification.push():
            if serializer.is_valid():
                serializer.save()
    
    def saveActivity2(self, request):
        self.__init__(request)
        serializer = ActivitySerializer(data=self.getData())
        if serializer.is_valid():
            serializer.save()
    
    @staticmethod
    def getActivities(id):
        result = []
        try: 
            activities = Activity.objects.filter(receiver_id=id)
            for activity in activities: 
                result.append({
                    "id": activity.id, 
                    "emitter": activity.emitter_id,
                    "receiver": activity.receiver_id, 
                    "task": activity.task,
                    "image": BASE + str(User.objects.get(id=activity.emitter_id).image),
                    "name": User.objects.get(id=activity.emitter_id).name,
                    "type": activity.type
                })
            return result
        except: 
            return result
    
    @staticmethod
    def deleteActivity(idf):
        Activity.objects.filter(id=idf).delete()
