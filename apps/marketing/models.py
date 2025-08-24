from django.db import models

# Create your models here.

from django.db import models

class CarouselSlide(models.Model):
    """
    Represents a single slide in the homepage carousel.
    """
    image = models.ImageField(upload_to='carousel/', help_text="Image for the carousel slide (e.g., 1920x800 pixels)")
    caption_header = models.CharField(max_length=200, blank=True, null=True, help_text="The main heading for the slide.")
    caption_text = models.TextField(blank=True, null=True, help_text="A short description or call to action.")
    link = models.URLField(blank=True, null=True, help_text="URL the slide links to (e.g., a product page).")
    display_order = models.PositiveIntegerField(default=0, help_text="Order in which the slide appears.")
    is_active = models.BooleanField(default=True, help_text="Is this slide currently visible on the site?")

    class Meta:
        ordering = ['display_order']
        verbose_name = "Carousel Slide"
        verbose_name_plural = "Carousel Slides"

    def __str__(self):
        return self.caption_header or f"Slide {self.id}"