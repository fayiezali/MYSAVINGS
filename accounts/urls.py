from django.urls import path
from django.contrib.auth import views as auth_views # This Views Built-in Django
from django.urls import reverse_lazy
from accounts import views
#
#
# 
#
#
#
#
# URL To Handle Password
urlpatterns = [
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        #The Full Name Of a Template To Use For GEnerating The Email With The Reset Password Link
        # The URL To Redirect To After a Successful Password Reset Request
        path('password-reset/'                             , auth_views.PasswordResetView.as_view(
                template_name='registration/my_password_reset.html', 
                subject_template_name='registration/my_password_reset_subject.txt',
                success_url= reverse_lazy('password_reset_done')),
                name='password_reset'),
                #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        path('password-reset/done/'                       , auth_views.PasswordResetDoneView.as_view(
                template_name='registration/my_password_reset_done.html'),
                name='password_reset_done'),
                #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        path('password-reset-confirm/<uidb64>/<token>/'  , auth_views.PasswordResetConfirmView.as_view(
                template_name='registration/my_password_reset_confirm.html'),
                name='password_reset_confirm'),
                #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        path('password-reset-complete/'                 , auth_views.PasswordResetCompleteView.as_view(
                template_name='registration/my_password_reset_complete.html'),
                name='password_reset_complete'),
]
#
#
# URL For Authentication (1) Login
urlpatterns += [
        # Login In System   
        path('accounts/my_login/'                  , views.My_Login.as_view()                  , name='My_Login_URL'),
        # Exit From System
        path('accounts/my_logout/'                 , views.My_Logout.as_view()                 , name='My_Logout_URL'),
        # Checkout Confirmed Successfull
        path('accounts/my_logout_done/'            , views.My_LogoutDone.as_view()             , name='My_LogoutDone_URL'),
]
#
#
# URL For Authentication (2)
urlpatterns += [
        # Change Password
        path('my_password_change/'                 , views.My_PasswordChange.as_view()         , name='My_PasswordChange_URL'),
        # Password Change completed Succesfull
        path('my_password_change_done/'            , views.My_PasswordChangeDone.as_view()     , name='My_PasswordChangeDone_URL'),
]


