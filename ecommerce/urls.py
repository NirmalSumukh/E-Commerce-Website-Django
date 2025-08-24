# ecommerce/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.apps import apps

oscar_app_config = apps.get_app_config('oscar')

urlpatterns = [
    # ====================================================================
    # Your Custom URLs
    # ====================================================================
    path('', include('apps.core.urls', namespace='core')),


    # ====================================================================
    # Oscar's URLs - Now included without the 'oscar' namespace
    # ====================================================================
    # By including only oscar_app_config.urls[0], we add all of Oscar's
    # URL patterns directly at the root. This makes namespaces like 'catalogue',
    # 'dashboard', and 'customer' available without the 'oscar:' prefix.
    path('', include(oscar_app_config.urls[0])),

    # This makes the 'marketing' namespace available to the dashboard.
    path('dashboard/marketing/', include(apps.get_app_config('marketing').urls[:2])),


    # ====================================================================
    # Other Project URLs
    # ====================================================================
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path("blog/",     include("apps.blog.urls")),
]

# This is important for serving user-uploaded files (like product images)
# and static files during development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
