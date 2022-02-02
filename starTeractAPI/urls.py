from django.urls import path
from . import views

urlpatterns = [
    path("signUp/", views.signUp),
    path("talents/", views.getTalents),
    path("joinAsTalent/", views.signUpAsTalent),
    path("login/", views.login),
    path("categories/", views.getCategories),
    path("auth/", views.checkValidToken),
    path("users/", views.getUserData),
    path("test/", views.test),
    path("talent/", views.getTalent),
    path("requestService/", views.requestService),
    path("notifications/<int:id>", views.getNotifications),
    path("checkNotifications/<int:id>", views.checkNotifications),
    path("getServices/<int:id>", views.getServices),
    path("refuseService/<int:id>/", views.refuseService)
]
