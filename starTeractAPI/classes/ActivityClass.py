from ..serializers import ActivitySerializer
from ..classes.NotificationClass import NotificationClass
from ..models import Activity, User

class ActivityClass: 
    id = 0
    user = 0
    talent = 0
    task = ""


    def __init__(self, request=None, activity=None):
        if request == None and activity == None: 
            pass
        elif request != None:
            self.id = Activity.objects.all().count() + 1
            self.user = request.get("activity").get("user")
            self.talent = request.get("activity").get("talent")
            self.task = request.get("activity").get("task")
    

    def getData(self): 
        return {
            "id": self.id,
            "user": self.user,
            "talent": self.talent,
            "task": self.task
        }
    
    def saveActivity(self, request):
        self.__init__(request)
        notification = NotificationClass(request)
        serializer = ActivitySerializer(data=self.getData())
        if notification.push():
            if serializer.is_valid():
                serializer.save()
    
    @staticmethod
    def getActivities(id):
        result = []
        try: 
            activities = Activity.objects.filter(user_id=id)
            for activity in activities: 
                result.append({
                    "id": activity.id, 
                    "user": activity.user_id,
                    "talent": activity.talent_id, 
                    "task": activity.task,
                    "image": User.objects.get(id=activity.talent_id).image,
                    "name": User.objects.get(id=activity.talent_id).name
                })
            return result
        except: 
            return result
    
    @staticmethod
    def deleteActivity(idf):
        Activity.objects.filter(id=idf).delete()
