from django.shortcuts import render
from django.views.generic import TemplateView , ListView ,DetailView , CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
#
"""
# The current user's permissions are stored in a template variable called {{ perms }}
# LoginRequiredMixin:
    Only a Logged In User Can Call This (Views)
# PermissionRequiredMixin:
    You Can check whether the Current User Has particular Permission
    Using variable Name {{ perms}} Within django "app"
"""
#
# 
# Display The Home Page
class Index(TemplateView):
    template_name = "commons/index.html" # The Page HTML to Display
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Number Of visits To The Site:
        # Get a Session Value Setting a Default If It Is Not Present.
        num_visits = self.request.session.get('num_visits', 1)
        # Render the HTML template index.html with the data in the context variable.
        context['number_of_visits_site'] =self.request.session['num_visits'] = num_visits+1 
        return context # Send This Data To The Required Page HTML
#
#
# Display Them About Page
class About(TemplateView):
    template_name = "commons/about.html" # The Page HTML to Display
#
#
#
def error_404(request, exception):
    context = {}
    return render(request,'commons/404.html' , context)

def error_500(request):
    context = {}
    return render(request,'commons/500.html', context)
