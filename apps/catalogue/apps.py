import oscar.apps.catalogue.apps as apps
from django.urls import path
from oscar.core.loading import get_class

# We DO NOT import the review view here anymore to prevent the AppRegistryNotReady error.

class CatalogueConfig(apps.CatalogueConfig):
    name = 'apps.catalogue'

    # The ready() method is no longer needed as we are defining the URL directly.

    def get_urls(self):
        """
        This is the final, corrected get_urls method.
        """
        # We now import the review view inside this method, which is only called
        # after all apps and models are fully loaded.
        from oscar.apps.catalogue.reviews.views import CreateProductReview

        # Load the standard views from their correct locations
        ProductListView = get_class('search.views', 'CatalogueView')
        CategoryView = get_class('search.views', 'ProductCategoryView')
        ProductDetailView = get_class('catalogue.views', 'ProductDetailView')

        urls = [
            path("", ProductListView.as_view(), name="index"),
            path(
                "<slug:product_slug>_<int:pk>/",
                ProductDetailView.as_view(),
                name="detail",
            ),
            path(
                "category/<slug:category_slug>/",
                CategoryView.as_view(),
                name="category",
            ),
            path(
                "category/<slug:category_slug>/<path:url>/",
                CategoryView.as_view(),
                name="category",
            ),

            # --- THIS IS THE NEW, DIRECT FIX ---
            # We are defining the 'reviews-add' URL directly within the catalogue app.
            # This bypasses all the complex forking and inclusion issues and
            # guarantees the URL exists where the template expects it.
            # Note: The URL pattern uses product_pk to match the template.
            path(
                '<slug:product_slug>_<int:product_pk>/reviews/add/',
                CreateProductReview.as_view(),
                name='reviews-add'
            ),
        ]

        return self.post_process_urls(urls)