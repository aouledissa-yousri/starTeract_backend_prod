from ..models import Video
from ..serializers import VideoSerializer
from ..classes.NotificationClass import NotificationClass 
from ..models import BASE

class VideoClass: 
    title = ""
    user = 0 
    talent = 0 
    video = None 

    def __init__(self, request=None):
        if request == None: 
            pass 
        else: 
            self.title = request.POST["title"]
            self.user = request.POST["user"]
            self.talent = request.POST["talent"]
            self.video = request.POST["video"]
    
    def getData(self):
        return {
            "title": self.title,
            "user": self.user,
            "talent": self.talent,
            "video": self.video
        }
    
    def addVideo(self, request):
        Video.objects.create(
            title = request.POST["title"],
            user_id = request.POST["user"],
            talent_id = request.POST["talent"],
            video = request.FILES["video"]
        )

        return True
    
    @staticmethod 
    def getVideos(id): 
        videos = []
        try: 
            records = Video.objects.filter(talent_id=id)
            for record in records: 
                videos.append({
                    "id": record.id,
                    "talent": record.talent_id,
                    "user": record.user_id,
                    "source": BASE + str(record.video),
                    "title": record.title,
                    "state": "pause",
                    "volume": "volume-mute",
                    "controls": False
                })
        except: 
            pass
        finally: 
            return videos
