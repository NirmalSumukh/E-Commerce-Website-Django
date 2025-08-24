# apps/catalogue/models.py

from django.urls import reverse
from oscar.apps.catalogue.abstract_models import (
    AbstractCategory,
    AbstractProduct,
    AbstractProductClass,
    AbstractProductAttribute,
    AbstractProductAttributeValue,
    AbstractAttributeOptionGroup,
    AbstractAttributeOption,
    AbstractOption,
    AbstractProductImage,
    AbstractProductCategory,
    AbstractProductRecommendation,
)

class Category(AbstractCategory):
    """
    This is the forked Category model.
    """
    def get_absolute_url(self):
        """
        This is the standard method for getting a category's URL.
        The 'oscar:' namespace has been removed.
        """
        if not self.slug:
            return ""
        return reverse('catalogue:category',
                       kwargs={'category_slug': self.slug})

    def _get_absolute_url(self, slug):
        """
        This is a private method used internally by the `category_tree`
        template tag. The 'oscar:' namespace has been removed.
        """
        if not slug:
            return ""
        return reverse('catalogue:category',
                       kwargs={'category_slug': slug})


class Product(AbstractProduct):
    """
    This is the forked Product model.
    We are overriding get_absolute_url and have removed the 'oscar:'
    namespace to match the new URL configuration.
    """
    def get_absolute_url(self):
        return reverse('catalogue:detail',
                       kwargs={'product_slug': self.slug, 'pk': self.pk})


# Re-declare other models so Django knows you're providing them
class ProductClass(AbstractProductClass): pass
class ProductAttribute(AbstractProductAttribute): pass
class ProductAttributeValue(AbstractProductAttributeValue): pass
class AttributeOptionGroup(AbstractAttributeOptionGroup): pass
class AttributeOption(AbstractAttributeOption): pass
class Option(AbstractOption): pass
class ProductImage(AbstractProductImage): pass
class ProductCategory(AbstractProductCategory): pass
class ProductRecommendation(AbstractProductRecommendation): pass
