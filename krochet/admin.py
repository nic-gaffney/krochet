from django.contrib import admin

from .models import Crochet, Order, SiteSettings

admin.site.register(Crochet)
admin.site.register(Order)
admin.site.register(SiteSettings)
# Register your models here.
