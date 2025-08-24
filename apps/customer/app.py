# apps/customer/app.py

# --- FIX: Correctly import the base application class for Oscar 4.0 ---
from oscar.apps.customer.apps import CustomerApplication as OscarCustomerApplication

class CustomerApplication(OscarCustomerApplication):
    """
    A custom customer app application class.

    This class allows us to override the default Oscar views with our own
    custom implementations. We are using properties to defer the import of
    the views until they are actually needed, which resolves the
    'AppRegistryNotReady' circular import error.
    """

    @property
    def register_view(self):
        # This property overrides the default registration view.
        # The import is done here, inside the property, so it only
        # happens when the URL is being resolved, not at startup.
        from .views import AccountRegistrationView
        return AccountRegistrationView

    @property
    def profile_update_view(self):
        # This property overrides the default profile update view.
        from .views import ProfileUpdateView
        return ProfileUpdateView

# Create an instance of our custom application class.
# Oscar will automatically discover and use this 'application' instance.
application = CustomerApplication()
