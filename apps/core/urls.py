from django.urls import path
from .views import HomeView, ContactView, newsletter_signup, PrivacyPolicyView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('newsletter-signup/', newsletter_signup, name='newsletter_signup'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
]