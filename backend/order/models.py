from django.db import models
from shop.models import Product, Option

class Order(models.Model):
    orderer_name     = models.CharField(max_length=99)
    orderer_number   = models.CharField(max_length=99)
    orderer_email    = models.EmailField(max_length=99)
    recipient_name   = models.CharField(max_length=99)
    recipient_number = models.CharField(max_length=99)
    address          = models.CharField(max_length=99)
    request          = models.CharField(max_length=99, null=True, blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    delivery_number  = models.CharField(max_length=99, null=True, blank=True)
    
    status_choices   = (
        ('WFP', 'WAITING_FOR_PAYMENT'),
        ('DP', 'DONE_PAYMENT'),
        ('IPD', 'IN_PROGRESS_DELIVERY'),
        ('DD', 'DONE_DELIVERY'),
        ('C', 'CANCLED'),
    )

    status           = models.CharField(max_length=99, choices=status_choices)

class ProductAndOption(models.Model):
    order   = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="product_and_options")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    option  = models.ForeignKey(Option, on_delete=models.DO_NOTHING)
