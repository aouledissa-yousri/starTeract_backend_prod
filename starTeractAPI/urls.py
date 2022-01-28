from django.urls import path
from . import views

urlpatterns = [
    path("signUp/", views.signUp),
    path("login/", views.test),
    path("joinAsTalent/", views.signUpAsTalent),
    #path("login/", views.login),
    path("categories/", views.getCategories),
    path("auth/", views.checkValidToken)
]
