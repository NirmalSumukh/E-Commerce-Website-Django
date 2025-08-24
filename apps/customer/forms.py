# apps/customer/forms.py

from django import forms
from phonenumber_field.formfields import PhoneNumberField

# --- FIX: Import the correct base registration form for Oscar 4.0 ---
from oscar.apps.customer.forms import EmailUserCreationForm as OscarRegistrationForm

from .models import Profile


class CustomRegistrationForm(OscarRegistrationForm):
    """
    A custom registration form that includes a phone number field.
    """
    phone_number = PhoneNumberField(
        region="IN",  # Set the default region to India
        widget=forms.TextInput(attrs={'placeholder': 'e.g., 9876543210'}),
        required=True,
        label="Phone Number"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # --- FIX ---
        # The phone_number field is automatically added by Django because it's
        # defined as a class attribute above. We no longer need to add it manually.
        # We just need to ensure the fields are in the order we want.
        # The parent form uses 'password1' and 'password2', not 'password_confirm'.
        self.order_fields(['email', 'phone_number', 'password1', 'password2'])


class ProfileUpdateForm(forms.ModelForm):
    """
    A form for users to update their profile, including their phone number.
    """
    class Meta:
        model = Profile
        fields = ['phone_number']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'e.g., 9876543210'}),
        }
