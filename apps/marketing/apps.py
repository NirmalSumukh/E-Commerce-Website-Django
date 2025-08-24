# apps/marketing/apps.py

from django.urls import path
from oscar.core.application import OscarDashboardConfig

# --- FIX: The import of views is moved inside the get_urls method ---
# from .views import (
#     CarouselListCreateView,
#     CarouselUpdateView,
#     CarouselDeleteView,
# )

class MarketingDashboardConfig(OscarDashboardConfig):
    """
    This is the AppConfig for the marketing dashboard app.
    It's responsible for registering the app with Oscar's dashboard
    and providing its URL patterns and permissions.
    """
    label = 'marketing'
    name = 'apps.marketing'
    verbose_name = 'Marketing'

    # By defining get_urls here, we register these URLs with Oscar's
    # dashboard permission system, which resolves the KeyError.
    def get_urls(self):
        # --- FIX: Import views here, inside the method ---
        # This prevents the AppRegistryNotReady error.
        from .views import (
            CarouselListCreateView,
            CarouselUpdateView,
            CarouselDeleteView,
        )
        
        urlpatterns = [
            path('carousel/', CarouselListCreateView.as_view(), name='manage_carousel'),
            path('carousel/update/<int:pk>/', CarouselUpdateView.as_view(), name='carousel-update'),
            path('carousel/delete/<int:pk>/', CarouselDeleteView.as_view(), name='carousel-delete'),
        ]
        return self.post_process_urls(urlpatterns)
