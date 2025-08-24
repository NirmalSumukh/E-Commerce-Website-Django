# Import the original Oscar views directly
from oscar.apps.catalogue import views as oscar_views

# In this version of Oscar, the catalogue app only contains the ProductDetailView.
# The list and category views are handled by the 'search' app.
# We only need to subclass the view that actually exists in this file.
class ProductDetailView(oscar_views.ProductDetailView):
    pass