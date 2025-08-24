# ecommerce/settings.py

import os
from oscar.defaults import *
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from oscar.defaults import OSCAR_DASHBOARD_NAVIGATION


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-your-secret-key-here' # Replace with a real secret key

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'haystack',

    # Your custom local apps
    'apps.core.apps.CoreConfig',
    'apps.blog.apps.BlogConfig',
    'apps.partners.apps.PartnersConfig',
    'apps.marketing.apps.MarketingDashboardConfig',
    
    # Manually listed Oscar apps. This is the correct method for Oscar 4.0.
    'oscar.config.Shop',
    'oscar.apps.analytics.apps.AnalyticsConfig',
    'apps.checkout.apps.CheckoutConfig', # Your forked checkout
    'oscar.apps.address.apps.AddressConfig',
    'apps.shipping.apps.ShippingConfig', #Forked Shipping App
    'apps.catalogue.apps.CatalogueConfig', # Your forked catalogue
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    'oscar.apps.partner.apps.PartnerConfig',
    'oscar.apps.basket.apps.BasketConfig',
    'oscar.apps.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    'apps.order.apps.OrderConfig', # Your forked order
    'apps.customer.apps.CustomerConfig', # Your forked customer
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'apps.dashboard.catalogue.apps.CatalogueDashboardConfig', # Your forked dashboard.catalogue
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',

     # 3rd-party apps
    'widget_tweaks',
    
    'treebeard',
    'sorl.thumbnail',
    'django_tables2',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_ckeditor_5',
    'django_filters',
    'taggit',
    'phonenumber_field',
]

# Required by Oscar
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Add Oscar's basket middleware
    'oscar.apps.basket.middleware.BasketMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Add the project-level templates directory
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # Add Oscar's context processors
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Authentication backends
# This is required for Oscar's dashboard to work
AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Oscar requires a search backend.
# For development, the Simple backend is easiest.
# HAYSTACK_CONNECTIONS setting
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

# This approach safely appends your custom navigation menu.
OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('Content Management'),
        'icon': 'fas fa-folder-open',
        'children': [
            {
                'label': _('Carousel Management'),
                'url_name': 'marketing:manage_carousel',
                # --- FIX THE LAMBDA FUNCTION HERE ---
                'access_fn': lambda user, *args, **kwargs: user.is_staff,
            },
            {
                'label': _('Blog Management'),
                'url_name': 'blog:staff_list',
                # --- AND FIX IT HERE ---
                'access_fn': lambda user, *args, **kwargs: user.is_staff,
            },
        ]
    }
)


# Crispy Forms Settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# --- Oscar Settings ---
OSCAR_SHOP_NAME = 'My Awesome Shop'
OSCAR_SHOP_TAGLINE = 'Great products, great prices'
OSCAR_DEFAULT_CURRENCY = 'INR'
# We use 'core:home' because your core app has the namespace 'core'.
OSCAR_HOMEPAGE = reverse_lazy('core:home')

#CKEditor Settings
CKEDITOR_UPLOAD_PATH = "blog/uploads/"
CKEDITOR_RESTRICT_BY_USER = True

#CKEditor Configuration
CKEDITOR_5_CONFIGS = {
    "blog": {
        "toolbar": [
            "heading", "|",
            "bold", "italic", "underline", "|",
            "link", "blockQuote", "|",
            "bulletedList", "numberedList", "|",
            "imageUpload", "insertTable", "mediaEmbed", "|",
            "undo", "redo", "sourceEditing"
        ],
        "image": { "toolbar": ["imageTextAlternative", "|",
                               "imageStyle:alignLeft", "imageStyle:alignRight", "imageStyle:side"] }
    }
}

#Razorpay Settings
RAZORPAY_KEY_ID     = os.environ.get("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET")


#BlueDart Settings
BLUEDART_API_LOGIN_ID = "YOUR_BLUEDART_LOGIN_ID"
BLUEDART_API_LICENSE_KEY = "YOUR_BLUEDART_LICENSE_KEY"
BLUEDART_API_CUSTOMER_CODE = "YOUR_CUSTOMER_CODE"
# Set to True for production, False for testing environment
BLUEDART_IS_PRODUCTION = False 