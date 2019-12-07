from django import template
from order.models import Order

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0

@register.filter
def cart_price_sum(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        sum=0
        sum1=0
        if qs.exists():
            for i in qs[0].items.all():
                sum1 = i.quantity * i.item.price
                sum = sum + sum1
            return sum
    return 0
    
@register.filter
def get_final_total(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        sum=0
        sum1=0
        if qs.exists():
            for i in qs[0].items.all():
                sum1 = i.quantity * i.item.price
                sum = sum + sum1
            return sum+30
    return 0