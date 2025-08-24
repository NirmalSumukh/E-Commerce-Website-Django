# apps/dashboard/catalogue/apps.py

from oscar.apps.dashboard.catalogue import apps as oscar_apps
from oscar.core.loading import get_class


class CatalogueDashboardConfig(oscar_apps.CatalogueDashboardConfig):
    name = 'apps.dashboard.catalogue'

    def ready(self):
        """
        This is the key change. We are moving the view definitions from the
        class level into the ready() method. This delays their loading
        until all apps are initialized, preventing the AttributeError.
        """
        super().ready()
        self.product_list_view = get_class('dashboard.catalogue.views', 'ProductListView')
        self.product_create_redirect_view = get_class('dashboard.catalogue.views', 'ProductCreateRedirectView')
        self.product_createupdate_view = get_class('dashboard.catalogue.views', 'ProductCreateUpdateView')
        self.product_delete_view = get_class('dashboard.catalogue.views', 'ProductDeleteView')

        self.category_list_view = get_class('dashboard.catalogue.views', 'CategoryListView')
        self.category_create_view = get_class('dashboard.catalogue.views', 'CategoryCreateView')
        self.category_update_view = get_class('dashboard.catalogue.views', 'CategoryUpdateView')
        self.category_delete_view = get_class('dashboard.catalogue.views', 'CategoryDeleteView')

        self.stock_alert_list_view = get_class('dashboard.catalogue.views', 'StockAlertListView')
        self.product_class_list_view = get_class('dashboard.catalogue.views', 'ProductClassListView')
        self.product_class_create_view = get_class('dashboard.catalogue.views', 'ProductClassCreateView')
        self.product_class_update_view = get_class('dashboard.catalogue.views', 'ProductClassUpdateView')
        self.product_class_delete_view = get_class('dashboard.catalogue.views', 'ProductClassDeleteView')
