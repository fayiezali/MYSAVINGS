from django.shortcuts import render #
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.contrib.auth import  get_user_model #
from django.contrib.auth.views import TemplateView #
from django.views import View #
from accounts.forms import SignUpForm #
from django.template.loader import render_to_string #
from django.contrib.sites.shortcuts import get_current_site #
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode #
from django.utils.encoding import force_bytes #
from django.contrib.auth.tokens import default_token_generator #
from django.core.mail import EmailMessage #
from django.contrib import messages
#
UserModel = get_user_model()
#
#
#
# Display Them About Page
class My_LogoutDone(TemplateView):
    template_name = 'registration/my_logout_done.html' # The Page HTML to Display
#
#
#
from django.contrib import messages
# 
# Register On The site And Create a Profile
class My_Signup(View):
    form_class = SignUpForm # Form for Entering New User Data
    template_name = 'registration/my_signup.html' # The Name Of a Template To Display For The View Use
    #
    # (1) Show User Registration Form
    def get(self, request, *args, **kwargs):
        form = self.form_class() # Save The Registration Form In a Variable
        return render(request, self.template_name, {'form': form})
    #
    # (2) Save Data and Send Email
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST) # Save The Registration Data In The Variable If It Is (POST)
        if form.is_valid(): # Verify That The Form Is Valid For Saving Its Data
            user = form.save(commit=False) # Stop Saving Data
            user.is_active = False # Deactivate The Account To Be Confirmed By Email
            user.save() # Save Data
            current_site = get_current_site(request) # Get the Current (Web Site) By Comparing The Domain With The Host Name
            subject = 'Activate Your ( My Saving ) Account' # Email Address
            message = render_to_string('registration/accounts_active_email.html', { # Email content
                'user': user,
                'domain': current_site.domain, # The Domain Name That Will Send The Message
                'uid': urlsafe_base64_encode(force_bytes(user.pk)), # URL Safe Encode
                'token': default_token_generator.make_token(user),}) # Create a Special Code Sent To The e-Mail To Activate The Account
            user.email_user(subject, message) # Send E-mail(content - Address)
            messages.success(request, ('Please Confirm Your Email To Complete Registration.'))# Display Message For The New User(In His Email)
            # Display Message For The New User On The Registration Page
            return render(request, 'registration/confirm_email_registration.html', {'message': f'A confirmation email has been sent to {user.email}. Please confirm to finish registering'})
        else:
            return render(request, self.template_name, {'form': form})
#
#
#
class Activate(View):
    def get(self, request, uidb64  , token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True # User Activation
            user.save() # Data Save
            # Show Confirm Email Registration Form And Dysplay Message For Successful Operation 
            return render(request, 'registration/confirm_email_registration_done.html', {'message': f'A confirmation email has been sent to {user.email}. Please confirm to finish registering'})
        else:
            # Show Activation Link Invalid Form For Unsuccessful Operation
            return render(request, 'registration/Activation_link_invalid.html')
#
#
#
