from oscar.apps.customer.models import * 
# apps/customer/models.py

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

# Oscar's user model is abstract, so we get the final one from settings
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    """
    A profile model that holds extra information for each user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Using PhoneNumberField for robust validation, especially for Indian numbers.
    # It will store numbers in a standardized international format (e.g., +91...).
    phone_number = PhoneNumberField(
        blank=True, 
        null=True, 
        help_text='Enter phone number in format: +919876543210'
    )

    def __str__(self):
        return f"{self.user.get_full_name()}'s Profile"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a Profile instance when a new User is created.
    """
    if created:
        Profile.objects.create(user=instance)
    # For existing users, just save the profile
    instance.profile.save()
