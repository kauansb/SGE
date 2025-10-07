from django.db.models.signals import post_save
from django.dispatch import receiver
from inflows.models import Inflow


@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.quantity += instance.quantity
        product.save()