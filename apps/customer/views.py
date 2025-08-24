# apps/customer/views.py

from oscar.apps.customer.views import AccountRegistrationView as OscarRegistrationView
from oscar.apps.customer.views import ProfileUpdateView as OscarProfileUpdateView
from django.urls import reverse_lazy

# Import your custom forms
from .forms import CustomRegistrationForm, ProfileUpdateForm
from .models import Profile

class AccountRegistrationView(OscarRegistrationView):
    """
    A custom registration view that uses our custom form.
    """
    form_class = CustomRegistrationForm
    template_name = 'oscar/customer/registration.html'

    def form_valid(self, form):
        # Let the parent class handle user creation
        response = super().form_valid(form)
        
        # Now, save the phone number to the user's profile
        phone_number = form.cleaned_data.get('phone_number')
        if phone_number:
            self.object.profile.phone_number = phone_number
            self.object.profile.save()
            
        return response


class ProfileUpdateView(OscarProfileUpdateView):
    """
    A custom profile update view that uses our profile form.
    """
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('customer:profile-view') # Redirect back to the profile page

    def get_object(self, queryset=None):
        # The object to be updated is the user's profile, not the user themselves
        return Profile.objects.get(user=self.request.user)
