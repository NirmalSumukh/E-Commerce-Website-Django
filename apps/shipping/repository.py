# apps/shipping/repository.py

from decimal import Decimal
from oscar.apps.shipping.repository import Repository as CoreRepository
from oscar.apps.shipping.methods import NoShippingRequired, Base
from oscar.core import prices

from .bluedart_client import bluedart_client

class Repository(CoreRepository):
    """
    This repository is responsible for returning a list of 
    available shipping methods.
    """
    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, **kwargs):
        # We REMOVE the check for a shipping_addr here.
        # Oscar needs a method even on the basket page before an address is entered.
        
        if basket.is_empty:
            return [NoShippingRequired()]

        # Always return the BlueDart method. Its `calculate` method will handle
        # the case where the address isn't known yet.
        return [BlueDartMethod(shipping_addr)]


class BlueDartMethod(Base):
    """
    A specific shipping method for BlueDart.
    """
    code = 'bluedart-standard'
    name = 'BlueDart Standard Shipping'

    # The shipping_addr can now be None
    def __init__(self, shipping_addr=None):
        self.shipping_addr = shipping_addr

    def calculate(self, basket):
        """
        Calculates the shipping charge. Returns a default price if no
        address is provided yet.
        """
        # Here, you could add logic: if self.shipping_addr, then call
        # the BlueDart API for a live quote based on the destination pincode.
        # For now, we return a fixed default price.
        charge = Decimal('150.00')
        return prices.Price(
            currency=basket.currency,
            excl_tax=charge,
            incl_tax=charge
        )

    def create_shipment(self, order, shipping_addr, **kwargs):
        """
        This method is called when an order is processed.
        It calls our client to book the shipment with BlueDart.
        """
        try:
            # Note: Oscar passes the final, validated shipping_addr to this method.
            awb_number, label_data = bluedart_client.create_shipment(order, shipping_addr)
            
            return {
                'tracking_number': awb_number,
                'tracking_url': f'https://www.bluedart.com/tracking?go=go&cn[]={awb_number}',
                'label_url': None, 
            }
        except Exception as e:
            # It's good practice to log this error properly
            print(f"Error creating BlueDart shipment for order {order.number}: {e}")
            return None
