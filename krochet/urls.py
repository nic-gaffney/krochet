from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:product_id>', views.shop, name='product'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.port, name='port'),
    path('paypal/', include("paypal.standard.ipn.urls")),
]
