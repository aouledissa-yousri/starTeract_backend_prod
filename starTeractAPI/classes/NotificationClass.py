from ..serializers import NotificationSerializer
from ..models import Notification

class NotificationClass: 
    id = 0
    description = ""
    checked = False
    reciever = 0 


    def __init__(self, request):
        self.id = Notification.objects.all.count()
        self.description = request.get("notification").get("description")
        self.checked = request.get("notification").get("checked")
        self.receiver = request.get("notification").get("receiver")
    
    def getNotificationData(self):
        return {
            "id": self.id,
            "description": self.description,
            "checked": self.checked,
            "user": self.receiver
        }
    
    def push(self):
        serializer = NotificationSerializer(data=self.getNotificationData())
        if serializer.is_valid():
            serializer.save()
        return serializer.is_valid()
