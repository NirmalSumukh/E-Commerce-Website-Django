import razorpay
from django.conf import settings
from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView
from oscar.apps.payment.models import Source, SourceType
from oscar.apps.payment.exceptions import UnableToTakePayment

class PaymentDetailsView(CorePaymentDetailsView):
    def handle_payment(self, order_number, total, **kwargs):
        # token/id sent from Razorpay Checkout.js
        rzp_payment_id = self.request.POST.get("razorpay_payment_id")
        if not rzp_payment_id:
            raise UnableToTakePayment("No Razorpay token")

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,
                                       settings.RAZORPAY_KEY_SECRET))
        client.payment.capture(rzp_payment_id, int(total.incl_tax * 100))
        source_type, _ = SourceType.objects.get_or_create(code='razorpay')
        source = Source(source_type=source_type,
                        currency=total.currency,
                        amount_allocated=total.incl_tax,
                        reference=rzp_payment_id)
        self.add_payment_source(source)
        self.add_payment_event('Settled', total.incl_tax)