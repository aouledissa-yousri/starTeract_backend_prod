import json
import jwt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User, Talent
from .classes.UserClass import UserClass
from .classes.TalentClass import TalentClass
from .classes.CategoryClass import CategoryClass
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def signUp(request):
    user = UserClass()
    if user.signUp(json.loads(request.body)):
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

@csrf_exempt
def signUpAsTalent(request):
    talent = TalentClass()
    if talent.signUp(json.loads(request.body)):
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})


@csrf_exempt
def login(request):
    talent = TalentClass()
    return JsonResponse(talent.login(json.loads(request.body)))

@csrf_exempt
def getCategories(request):
    return JsonResponse(CategoryClass.getCategories(), safe=False)

@csrf_exempt
def printCategories(request):
    return JsonResponse(json.loads(request.body).get("categories"), safe=False)

@csrf_exempt
def test(request):
    return JsonResponse((json.loads(request.body)), safe=False)

@csrf_exempt
def checkValidToken(request):
    try:
        decodedToken = jwt.decode(json.loads(request.body).get("token"), "success", algorithms=["HS256"])
        return JsonResponse({"message": "token is valid"}, safe=False)
    except:
        return JsonResponse({"message": "invalid token"}, safe=False)

#@csrf_exempt
def test(request):
    return render(request, "login.html")




