# apps/marketing/views.py

from django.urls import reverse_lazy
from django.views import generic

# The security is now handled in app.py, so we no longer need decorators here.
# from django.contrib.admin.views.decorators import staff_member_required
# from django.utils.decorators import method_decorator

from .models import CarouselSlide
from .forms import CarouselSlideForm

class CarouselListCreateView(generic.CreateView):
    model = CarouselSlide
    form_class = CarouselSlideForm
    template_name = 'oscar/dashboard/marketing/carousel_management.html'
    success_url = reverse_lazy('marketing:manage_carousel')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = CarouselSlide.objects.all().order_by('display_order')
        context['form_title'] = 'Create New Slide'
        return context

class CarouselUpdateView(generic.UpdateView):
    model = CarouselSlide
    form_class = CarouselSlideForm
    template_name = 'oscar/dashboard/marketing/carousel_management.html'
    success_url = reverse_lazy('marketing:manage_carousel')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = CarouselSlide.objects.all().order_by('display_order')
        context['form_title'] = f"Update Slide: {self.object.caption_header}"
        return context

class CarouselDeleteView(generic.DeleteView):
    model = CarouselSlide
    template_name = 'oscar/dashboard/marketing/carousel_confirm_delete.html'
    success_url = reverse_lazy('marketing:manage_carousel')
