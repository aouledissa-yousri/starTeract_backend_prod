import hashlib

class Credentials:
    __name = ""
    __email = ""
    __password = ""

    def __init__(self, request):
        self.__name = request.POST.get("username")
        self.__email = request.POST.get("username")
        self.__password = Credentials.hash(request.POST.get("password"))
    
    @classmethod
    def hash(self, text):
        result = hashlib.sha256(text.encode())
        return result.hexdigest()
    
    def getCredentials(self):
        return {
            "name":  self.__name,
            "email":  self.__email,
            "password":  self.__password
        }
    
   