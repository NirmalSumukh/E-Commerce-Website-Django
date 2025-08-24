from django.contrib import admin

# Register your models here.
from .models import CarouselSlide

@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CarouselSlide model.
    """
    list_display = ('caption_header', 'display_order', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('caption_header', 'caption_text')
    list_editable = ('display_order', 'is_active')
    ordering = ('display_order',)

