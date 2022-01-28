import hashlib

class Credentials:
    __name = ""
    __email = ""
    __password = ""

    def __init__(self, request):
        self.__name = request.get("name")
        self.__email = request.get("email")
        self.__password = request.get("password")
    
    def getCredentials(self):
        return {
            "name":  self.__name,
            "email":  self.__email,
            "password":  self.__password
        }
    
   