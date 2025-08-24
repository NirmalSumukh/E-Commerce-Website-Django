# apps/customer/urls.py

from django.urls import path
from oscar.core.application import OscarDashboardConfig
from .views import AccountRegistrationView, ProfileUpdateView

class CustomerDashboardApplication(OscarDashboardConfig):
    # This ensures that any dashboard URLs from the original customer app are included
    # if you decide to customize them later.
    pass

# We are only overriding the specific views we need to change.
# Oscar's get_core_apps function will pick up the rest.
register_view = AccountRegistrationView.as_view()
profile_update_view = ProfileUpdateView.as_view()

# Define the custom URL patterns for the views we have overridden.
# The names ('register', 'profile-update') must match Oscar's default names.
custom_urlpatterns = [
    path('accounts/register/', register_view, name='register'),
    path('accounts/profile/', profile_update_view, name='profile-update'),
]

# The on_init method is used by Oscar to collect the final list of URLs.
on_init = OscarDashboardConfig.on_init
