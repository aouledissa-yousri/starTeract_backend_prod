from django.shortcuts import render, redirect
from .models import User, Talent
from .classes.UserClass import UserClass
from .classes.TalentClass import TalentClass


# Create your views here.

def signUp(request):
    if request.method == 'POST':
        user = UserClass()
        if user.signUp(request):
            return redirect("../success/")
    return render(request, "signUp.html")

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
            return redirect("../success/")
        else:
            return redirect("../fail/")
    return render(request, "login.html")


def success(request):
    return render(request, "success.html")

def failure(request):
    return render(request, "fail.html")


