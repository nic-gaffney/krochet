from django import forms
from django.forms import ModelForm
from django.views.generic import FormView
from paypal.standard.forms import PayPalPaymentsForm
from django.utils.html import format_html
from .models import Address


class CustomPayPalPaymentsForm(PayPalPaymentsForm):
    def get_html_submit_element(self):
        return """<button type="submit" class="f6 link dim ph3 pv2 mb2 dib white bg-black">Continue on PayPal website</button>"""


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ("street", "city", "state", "code")
