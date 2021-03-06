from rest_framework import serializers
from .models import User, Talent, Category, Classification, Service, Notification, Activity, Video, Review, Payment

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

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Review
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Payment
        fields = "__all__"

