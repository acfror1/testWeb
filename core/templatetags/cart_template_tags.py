from django import template
from core.models import Order, OrderItem

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        od = OrderItem.objects.filter(
            user=user,
            ordered=False
        )
        total = 0
        for o in od:
            total += o.quantity
        if qs.exists():
            return total
    return 0


def cart_item(user):

    od = OrderItem.objects.filter(
        user=user,
        ordered=False
    )

    return od.item.all
