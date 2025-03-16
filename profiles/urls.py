from django.urls import path
from . import views

urlpatterns = [
    path("",views.CreateProfileVieew.as_view()),
    path("lists",views.ProfileView.as_view())
]

