import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User, Talent
from .classes.UserClass import UserClass
from .classes.TalentClass import TalentClass
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def signUp(request):
    user = UserClass()
    if user.signUp(json.loads(request.body)):
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

def signUpAsTalent(request):
    if request.method == "POST":
        talent = TalentClass()
        if talent.signUp(request):
            return redirect("../success/")
    return render(request, "JoinAsTalent.html")



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


