from django.urls import path
from django.contrib.auth import views as auth_views # This Views Built-in Django
from accounts import views
#
#
# 
#
#
# URL For Authentication (1)
urlpatterns = [
        # Login In System   
        path('accounts/my_login/'                            , views.My_Login.as_view()                  , name='My_Login_URL'),
        # Exit From System
        path('accounts/my_logout/'                           , views.My_Logout.as_view()                 , name='My_Logout_URL'),
        # Checkout Confirmed Successfull
        path('accounts/my_logout_done/'                      , views.My_LogoutDone.as_view()             , name='My_LogoutDone_URL'),
        #*********************************************************************************
        # # Change Password
        # path('my_password_change/'                 , views.My_PasswordChange.as_view()         , name='My_PasswordChange_URL'),
        # # Password Change completed Succesfull
        # path('my_password_change_done/'            , views.My_PasswordChangeDone.as_view()     , name='My_PasswordChangeDone_URL'),
]
#
#
# URL For Authentication (2)

