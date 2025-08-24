# apps/customer/apps.py

from oscar.apps.customer import apps as oscar_apps

class CustomerConfig(oscar_apps.CustomerConfig):
    """
    This is the Django AppConfig for your forked customer app.
    """
    # This name is important and should match the app's location.
    name = 'apps.customer'

    # --- CRITICAL FIX ---
    # This line tells Oscar to look for the view and URL logic in the
    # 'application' instance within your 'apps/customer/app.py' file.
    # This resolves the circular import and AppRegistryNotReady errors.
    application = 'apps.customer.app.application'

    def ready(self):
        # This method is called when Django is ready.
        # It's a safe place to import and connect signals in the future.
        super().ready()
        # from . import signals
