from ..serializers import ReviewSerializer
from ..models import Talent, Review

class ReviewClass:
    comment = ""
    rating = 0
    user = 0 
    talent = 0 

    def __init__(self, request=None):
        if request == None:
            pass 
        elif request != None: 
            self.comment = request.get("comment")
            self.rating = request.get("rating") 
            self.user = request.get("user")
            self.talent = request.get("talent") 
    

    def getData(self):
        return {
            "user": self.user,
            "talent": self.talent,
            "comment": self.comment,
            "rating": self.rating,
        }
    

    def postReview(self, request):
        self.__init__(request)
        serializer = ReviewSerializer(data=self.getData())
        if serializer.is_valid():
            serializer.save()
            Talent.objects.filter(user_ptr_id=self.talent).update(rating = self.updateTalentRating())
        return serializer.is_valid()
    
    def updateTalentRating(self):
        rating = 0 
        reviews = Review.objects.filter(talent_id=self.talent) 
        for review in reviews: 
            rating += review.rating
        return (rating / reviews.count())