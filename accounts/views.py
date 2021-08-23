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
from django.utils import timezone
from django.views.generic import TemplateView , ListView ,DetailView , DeleteView, UpdateView  , FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#
UserModel = get_user_model()
#
#
#
# Display The my_Profile_delete_done Page
class My_LogoutConfirm(TemplateView):
    template_name = 'registration/my_logout_confirm.html' # The Page HTML to Display
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
            # Reload The Form  Registration Agin
            return render(request, self.template_name, {'form': form})
#
#
#
# Activate E-mail
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
#
#
#
# Display List Record
class my_profile_list(LoginRequiredMixin , ListView):
    model = User # Data Table
    paginate_by = 4  # if pagination is desired
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now() # Data To Be Sent To Page HTML
        return context # Send This Data To The Required Page HTML
    template_name = 'registration/my_profile_list.html'# The Page HTML to Display
#
#
#
#
#
#
# Display Detail Record By: Slug
class My_Profile_Detail_Slug(LoginRequiredMixin ,  DetailView):
    model = User # Data Table
    slug_field = 'ASS_Slug' # Filter Field Use 'Slug'
    context_object_name = 'My_Object' # Data To Be Sent To Page HTML
    template_name = 'registration/my_profile_detail_slug.html'# The Page HTML to Display
#
#
#
## Display Detail Record By: ID
class My_Profile_Detail_ID(LoginRequiredMixin , DetailView):
    model = User # Data Table
    slug_field = 'pk' # Filter Field Use 'PK"
    context_object_name = 'My_Object' # Data To Be Sent To Page HTML
    template_name = 'registration/my_profile_detail_ID.html'# The Page HTML to Display
#
#
#
# Update Profile.
class My_Profile_Update(UpdateView):
        model = User # Data Table
        fields = [ # Fields Table
            'last_login',
            'is_superuser', 
            'username', 
            'last_name',
            'email',
            'is_staff', 
            'is_active', 
            'date_joined',
            'first_name',
            ]
        template_name = 'registration/My_Profile_Update.html'# The Page HTML to Display
        success_url = reverse_lazy('my_profile_list_URL')# Go to This Page After Successful Operation
#
#
#
# Delete Record.
class My_Profile_Delete(LoginRequiredMixin  , DeleteView):
    model = User # Data Table
    template_name = 'registration/my_profile_confirm_delete.html' # The Page HTML to Display
    success_url = reverse_lazy('My_Profile_Delete_Done_URL') # Go to This Page After Successful Operation
#
#
#
# Display The my_Profile_delete_done Page
class My_Profile_Delete_Done(TemplateView):
    template_name = 'registration/my_profile_delete_done.html' # The Page HTML to Display
#
#

