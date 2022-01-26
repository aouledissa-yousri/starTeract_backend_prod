from rest_framework import serializers
from .models import User, Talent, Category, Classification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = "__all__"

