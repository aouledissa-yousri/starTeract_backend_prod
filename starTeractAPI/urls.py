from django.urls import path
from . import views

urlpatterns = [
    path("signUp/", views.signUp),
    path("talents/", views.getTalents),
    path("joinAsTalent/", views.signUpAsTalent),
    path("login/", views.login),
    path("categories/", views.getCategories),
    path("auth/", views.checkValidToken),
    path("users/", views.getUserData)
]
