from django.db.models.signals import post_save
from django.dispatch import receiver
from outflows.models import Outflow


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    # created true (novo registro) false (é um update!)
    if created:
        if instance.quantity > 0:
            product = instance.product             # pega instancia de produto
            product.quantity -= instance.quantity  # subtrai pois estamos em outflow
            product.save()                         # salva novo estoque