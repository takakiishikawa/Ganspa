from django.urls import path
from.import views

urlpatterns=[
    path("top/",views.top,name="top"),
    path("guide/",views.guide,name="guide"),
    path("users/",views.users,name="users"),
    path("user/",views.user,name="user"),
    path("register/",views.AccountRegistration.as_view(),name="registration")
    path("create",views.create,name="create")
]
