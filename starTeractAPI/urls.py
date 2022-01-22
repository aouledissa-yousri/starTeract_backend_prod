from django.urls import path
from . import views

urlpatterns = [
    path("signUp/", views.signUp),
    path("joinAsTalent/", views.signUpAsTalent),
    path("login/", views.login),
    path("success/", views.success),
    path("fail/", views.failure)
]
