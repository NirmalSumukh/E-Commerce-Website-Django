# # ecommerce/urls.py

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.apps import apps

# # --- FIX: Import your new marketing dashboard application ---
# from apps.marketing.app import application as marketing_app

# urlpatterns = [
#     # Your Custom URLs
#     path('', include('apps.core.urls', namespace='core')),
    
#     # --- FIX: Include your marketing app's URLs here ---
#     # This now correctly registers the app and its permissions with the dashboard.
#     path('dashboard/marketing/', marketing_app.urls),

#     # Oscar's URLs
#     path('', include(apps.get_app_config('oscar').urls[0])),

#     # Other Project URLs
#     path('admin/', admin.site.urls),
#     path('i18n/', include('django.conf.urls.i18n')),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
