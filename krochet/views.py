from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.template import RequestContext
from .models import Crochet, Order, Address
from .forms import CustomPayPalPaymentsForm, AddressForm
import random


def index(request):
    products = Crochet.objects.all()

    return render(request, 'index.html',
                  {
                      'plush': products[random.randint(0, len(products)-1)]
                  }
                  )


def shop(request, product_id=0, addr=None):
    products = Crochet.objects.all()

    try:
        obj = Crochet.objects.get(pk=product_id)
        order = Order()
        order.obj = obj
        order.getInvoice()

        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": obj.price,
            "item_name": obj.name,
            "invoice": f"{product_id}::{order.date}",
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return": request.build_absolute_uri(reverse('index')),
            "cancel_return": request.build_absolute_uri(reverse('shop')),
        }
        # print(f"order.date = {order.date}")
        # print("invoice = {0}".format(paypal_dict['invoice']))

        # Create the instance.
        form = CustomPayPalPaymentsForm(initial=paypal_dict)

        context = {"form": form, 'product': obj}
        context['addr'] = AddressForm()
        context['addrF'] = True
        if request.method == 'POST':
            addrForm = AddressForm(request.POST)
            if addrForm.is_valid():
                addr = addrForm.save()
                addr.save()
                order.address = addr
                order.save()

            context['addrF'] = False
            return render(request, 'shop/product.html', context)

        return render(request, 'shop/product.html', context)

    except Crochet.DoesNotExist:
        return render(request, 'shop/index.html', {
            'products': products
        })
