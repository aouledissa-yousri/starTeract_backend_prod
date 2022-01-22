from rest_framework import serializers
from .models import User, Talent

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = "__all__"

