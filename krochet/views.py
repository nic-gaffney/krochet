from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from .models import Crochet, Order
from .forms import CustomPayPalPaymentsForm
import random


def index(request):
    products = Crochet.objects.all()

    return render(request, 'index.html',
                  {
                      'plush': products[random.randint(0, len(products)-1)]
                  }
                  )


def shop(request, product_id=0):
    products = Crochet.objects.all()

    try:
        obj = Crochet.objects.get(pk=product_id)
        order = Order()
        order.obj = obj
        order.getInvoice()
        order.save()
        # addr = AddressForm()

        # if addr.is_valid():
        #     city = form.cleaned_data['city']
        #     state = form.cleaned_data['state']
        #     street = form.cleaned_data['street']
        #     code = form.cleaned_data['code']

        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": obj.price,
            "item_name": obj.name,
            "invoice": f"{product_id}::{order.date}",
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return": request.build_absolute_uri(reverse('index')),
            "cancel_return": request.build_absolute_uri(reverse('shop')),
        }
        print(f"order.date = {order.date}")
        print("invoice = {0}".format(paypal_dict['invoice']))

        # Create the instance.
        form = CustomPayPalPaymentsForm(initial=paypal_dict)
        context = {"form": form, 'product': obj}
        # makeOrder(addr, obj)
        return render(request, 'shop/product.html', context)

    except Crochet.DoesNotExist:
        return render(request, 'shop/index.html', {
            'products': products
        })
