from django.db import models
# Create your models here.


class Crochet(models.Model):
    name = models.CharField(max_length=70)
    picture = models.ImageField(
        upload_to=f'static/images/', height_field=None, width_field=None, max_length=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    info = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    obj = models.ForeignKey(
        "krochet.Crochet", verbose_name=("Crochet Requested"), on_delete=models.CASCADE)
    address = models.ForeignKey(
        "krochet.Address", verbose_name=("Order Address"), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, editable=False)
    paid = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"INVOICE: {self.obj.id}::{self.date}\t PAID: {self.paid}\t ADDR: {self.address} FIN: {self.completed}"

    def getInvoice(self):
        self.invoice = f"{self.obj.id}::{self.date}"
        return self.invoice


class Address(models.Model):
    street = models.CharField(max_length=75)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=30)
    code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.code}"
