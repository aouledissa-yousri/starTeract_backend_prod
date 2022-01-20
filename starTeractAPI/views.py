from django.shortcuts import render
from .models import User, Talent
from .serializers import UserSerializer, TalentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def signUp(request):
    if request.method == 'POST':
        user = User()
        serializer = UserSerializer(data=user.getData(request))
        if serializer.is_valid():
            serializer.save()
    return render(request, "signUp.html")

def signUpAsTalent(request):
    if request.method == 'POST':
        talent = Talent()
        serializer = TalentSerializer(data=talent.getData(request))
        if serializer.is_valid():
            serializer.save()
    return render(request, "JoinAsTalent.html")
