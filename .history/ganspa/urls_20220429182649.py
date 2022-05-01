from django.urls import path
from.import views

urlpatterns=[
    path("top/",views.top,name="top"),
    path("guide/",views.guide,name="guide"),
    path("users/",views.users,name="users"),
    path("user/",views.user,name="user"),
    path("login/",views.user,name="user"),
    path("register/",views.user,name="user"),

    
    ]
