from django import forms
from .models import CarouselSlide

class CarouselSlideForm(forms.ModelForm):
    class Meta:
        model = CarouselSlide
        fields = ['image', 'caption_header', 'caption_text', 'link', 'display_order', 'is_active']