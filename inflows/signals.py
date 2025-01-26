from django.db.models.signals import post_save
from django.dispatch import receiver
from inflows.models import Inflow


@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    # created true (novo registro) false (é um update!)
    if created:
        if instance.quantity > 0:
            product = instance.product             # pega instancia de produto
            product.quantity += instance.quantity  # soma pois estamos em inflow
            product.save()                         # salva novo estoque
