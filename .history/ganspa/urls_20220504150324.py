from django.urls import path
from.import views
from django.contrib.auth import views as auth_views 


urlpatterns=[
    path("top/",views.top,name="top"),
    path("guide/",views.guide,name="guide"),
    path("users/",views.users,name="users"),
    path("user/",views.user,name="user"),
    path("register/",views.AccountRegistration.as_view(),name="registration"),
    path('accounts/password_change_form/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change_form'),    # 追加
    path('accounts/password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_finish.html'), name='password_change_done'), # 追加
]
