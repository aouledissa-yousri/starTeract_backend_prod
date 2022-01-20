from django.urls import path
from . import views

urlpatterns = [
    path("signUp/", views.signUp),
    path("joinAsTalent/", views.signUpAsTalent)
]
