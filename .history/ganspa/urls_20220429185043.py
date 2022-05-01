from django.urls import path
from.import views

urlpatterns=[
    path("top/",views.top,name="top"),
    path("guide/",views.guide,name="guide"),
    path("users/",views.users,name="users"),
    path("user/",views.user,name="user"),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("form/",views.form,name="form"),
    
    ]
