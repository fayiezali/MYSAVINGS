from django.shortcuts import render
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.contrib.auth.views import LoginView , LogoutView ,TemplateView
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
