import json
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



def login(request):
    if request.method == "POST":
        user = UserClass()
        if user.login(request):
            return redirect("../success")
        else:
            return redirect("../fail/")
    return render(request, "login.html")


def success(request):
    return render(request, "success.html")

def failure(request):
    return render(request, "fail.html")

@csrf_exempt
def getCategories(request):
    return JsonResponse(CategoryClass.getCategories(), safe=False)

@csrf_exempt
def printCategories(request):
    return JsonResponse(json.loads(request.body).get("categories"), safe=False)








'''def test(request):
    categories = [
        "Sport",
        "Politics",
        "Science",
        "International star",
        "Khaleej",
        "Signer",
        "Actor",
        "TV",
        "Musician",
        "Rapper",
        "Metal",
        "Rock",
        "For kids",
        "Media",
        "Comedian",
        "Content creator",
        "Youtuber",
        "Poet",
        "Marketing",
    ]

    for i in range(0,len(categories)):
        category = CategoryClass(categories[i])
        category.save()'''
        


