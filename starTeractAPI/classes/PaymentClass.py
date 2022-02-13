from ..classes.ActivityClass import ActivityClass
from ..classes.NotificationClass import NotificationClass
from ..serializers import PaymentSerializer
from ..models import Activity, Payment


class PaymentClass(ActivityClass):
    paymentLink = ""


    def __init__(self, request = None):
        if request == None: 
            pass
        else:
            super().__init__(request) 
            self.paymentLink = request.get("activity").get("paymentLink")
    

    def getData(self): 
        data = super().getData()
        data["paymentLink"] = self.paymentLink
        return data
    
    def saveActivity(self, request):
        self.__init__(request)
        notification = NotificationClass(request)
        serializer = PaymentSerializer(data=self.getData())
        if notification.push():
            if serializer.is_valid():
                serializer.save()
    
    def getPaymentLink(id):
        payment = Payment.objects.get(activity_ptr_id=id)
        return {
            "link": payment.paymentLink
        }