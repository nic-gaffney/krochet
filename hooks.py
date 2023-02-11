from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from krochet.models import Crochet, Order
import logger


def paypal_payment_received(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != 'sb-v52uo25037825@business.example.com':
            # Not a valid payment
            return

        # ALSO: for the same reason, you need to check the amount
        # received, `custom` etc. are all what you expect or what
        # is allowed.
        try:
            my_pk = ipn_obj.invoice[0]
            print(f"IPN_OBJ.INVOICE = {ipn_obj.invoice}")
            mytransaction = Crochet.objects.get(pk=my_pk)
            print(
                f"{ipn_obj.mc_gross} == {mytransaction.price} and {ipn_obj.mc_currency} == 'USD'")
            assert ipn_obj.mc_gross == mytransaction.price and ipn_obj.mc_currency == 'USD'
        except Exception:
            print(f'Paypal ipn_obj data not valid! {Exception}')
        else:
            orders = Order.objects.all()
            for o in orders:
                if o.getInvoice() == ipn_obj.invoice:
                    o.paid = True
                    o.save()
                    print(o)
    else:
        print('Paypal payment status not completed: %s' %
              ipn_obj.payment_status)


valid_ipn_received.connect(paypal_payment_received)
print("READY")
