# apps/core/views.py

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.http import require_POST

# Import the Product model from your forked catalogue app
from apps.catalogue.models import Product
from apps.marketing.models import CarouselSlide
# Your other imports for the contact form
from .forms import ContactForm
from .models import ContactMessage


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        """
        Adds carousel slides, featured products, and latest posts to the context.
        """
        context = super().get_context_data(**kwargs)

        # --- MODIFICATION: Fetch active carousel slides ---
        # Get all slides that are marked as 'active' and order them.
        context['carousel_slides'] = CarouselSlide.objects.filter(is_active=True).order_by('display_order')

        # Fetch the first 6 products from Oscar's catalogue to display.
        try:
            context['featured_products'] = Product.objects.filter(is_public=True)[:6]
        except Product.DoesNotExist:
            context['featured_products'] = []

        return context


class ContactView(TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message here later
            return redirect('core:contact')
        return render(request, self.template_name, {'form': form})

# --- FIX: Re-adding the missing views ---

class PrivacyPolicyView(TemplateView):
    """
    A simple view to render the privacy policy page.
    """
    template_name = "core/privacy_policy.html"


@require_POST
def newsletter_signup(request):
    """
    A view to handle the newsletter signup form submission.
    """
    email = request.POST.get('email')
    if email:
        # Here you would add your logic to save the email,
        # for example, to a NewsletterSignup model.
        print(f"New newsletter signup: {email}") # Prints to your console for now
        # You should redirect the user back to the homepage, maybe with a success message.
        return redirect('core:home')
    # Handle case where email is not provided
    return HttpResponse("Please provide a valid email address.", status=400)

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    try:
        products = Product.objects.filter(is_public=True)[:6]

        # DEBUG: Check which product (if any) causes decoding issues
        for p in products:
            print(f"ID: {p.id}, Title: {p.title}")  # Add other fields like p.description if needed

        context['featured_products'] = products

    except Exception as e:
        print("Error while fetching products:", e)
        context['featured_products'] = []

    return context