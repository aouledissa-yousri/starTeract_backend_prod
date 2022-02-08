from ..serializers import NotificationSerializer
from ..models import Notification, User
from ..models import BASE


class NotificationClass: 
    id = 0
    description = ""
    checked = False
    receiver = 0 
    emitter = 0
    image = ""


    def __init__(self, request=None, notification=None):
        if notification == None and request==None:
            pass
        elif request != None and notification == None:
            self.id = Notification.objects.all().count() + 1
            self.description = request.get("notification").get("description")
            self.checked = request.get("notification").get("checked")
            self.receiver = request.get("notification").get("receiver")
            self.emitter = request.get("notification").get("emitter")
        elif notification != None:
            self.id = notification.id
            self.description = notification.description
            self.checked = notification.checked
            self.receiver = notification.user_id
            self.emitter = notification.emitter_id
    
    def getNotificationData(self):
        return {
            "id": self.id,
            "description": self.description,
            "checked": self.checked,
            "user": self.receiver,
            "emitter": self.emitter,
            "image": BASE + str(User.objects.get(id=self.emitter).image)
        }
    
    def getNotificationData2(self):
        return {
            "id": self.id,
            "description": self.description,
            "checked": self.checked,
            "user": self.receiver,
            "emitter": self.emitter,
        }
    
    def push(self):
        serializer = NotificationSerializer(data=self.getNotificationData2())
        if serializer.is_valid():
            serializer.save()
        return serializer.is_valid()
    
    @staticmethod
    def getNotifications(id):
        try: 
            notifications = Notification.objects.filter(user_id=id)
            result = []
            for notification_ in notifications:
                notification = NotificationClass(None,notification_)
                result.append(notification.getNotificationData())
            return result 
        except:
            return None
    
    @staticmethod
    def checkNotifications(id):
        Notification.objects.filter(checked=False, user_id=id).update(checked=True)
