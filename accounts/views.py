from django.shortcuts import render
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.contrib.auth.views import ( LoginView , LogoutView ,
                                        TemplateView , PasswordChangeView
)
from django.urls import reverse_lazy

#
#
#
#
#
#
# Log In The System
class My_Login(LoginView):
    template_name = 'registration/my_login.html'  # The Page HTML to Display
#
#
#
# Log Out Of The System:
class My_Logout(LogoutView):
    pass
#
#
#
# Display Them About Page
class My_LogoutDone(TemplateView):
    template_name = 'registration/my_logout_done.html' # The Page HTML to Display
#
#
#
# Confirm Checkout From System
class My_PasswordChange(PasswordChangeView):
    template_name = 'registration/my_password_change.html' # The Page HTML to Display
    success_url = reverse_lazy('My_PasswordChangeDone_URL') # Go to This Page After Successful Operation
#
#
#
#Confirm Password Change
class My_PasswordChangeDone(TemplateView):
    template_name = 'registration/my_password_change_done.html'# The Page HTML to Display
    # title = ('password change successful')
#
#
#
