from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product
from order.models import Order, OrderItem 
from django.utils import timezone
from django.contrib import messages

def cart(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        context = {
            'object':order
        }
        return render(request,'order/cart.html',context)
    except ObjectDoesNotExist:
        messages.error(request,"You do not have an active order")
        return redirect("/")

def add_to_cart(request,product_id):
    if request.user.is_authenticated:
        item = get_object_or_404(Product, pk=product_id)
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(user = request.user, ordered = False)
        if order_qs.exists():
            order = order_qs[0]
            #check if the order item is in the order
            if order.items.filter(item__id = item.id).exists():
                order_item.quantity += 1
                order_item.save()
                messages.success(request, 'This item quantity was updated')
                return redirect("cart")
            else:
                order.items.add(order_item)
                messages.success(request, 'This item was added to your cart')
                return redirect("/products/"+ str(product_id))

        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user = request.user, ordered_date = ordered_date)
            order.items.add(order_item)
            messages.success(request, 'This item was added to your cart')
            return redirect("/products/"+ str(product_id))
    else:
        return redirect('login')

def remove_from_cart(request,product_id):
    if request.user.is_authenticated:
        item = get_object_or_404(Product, pk=product_id)
        order_qs = Order.objects.filter(user = request.user, ordered = False)
        if order_qs.exists():
            order = order_qs[0]
            #check if the order item is in the order
            if order.items.filter(item__id = item.id).exists():
                order_item= OrderItem.objects.filter(
                        item=item,
                        user=request.user,
                        ordered=False
                    )[0]
                order_item.delete()
            # order.items.remove(order_item)
                messages.success(request, 'This item was removed to your cart')
                return redirect("cart")
            else:
                #add a message that user does not contain order item
                messages.error(request, 'This item was not in your cart')
                return redirect("/products/"+ str(product_id))    
        else:
            #add a message that user does not have an order
            messages.error(request, 'You do not have an active order')
            return redirect("/products/"+ str(product_id)) 
    else:
        return redirect('login')   

def remove_singal_item_from_cart(request,product_id):
    item = get_object_or_404(Product, pk=product_id)
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__id = item.id).exists():
            order_item= OrderItem.objects.filter(
                    item=item,
                    user=request.user,
                    ordered=False
                )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.success(request, 'The item quantity was updated')
                return redirect("cart")
            else:
                order.items.remove(order_item)
                return redirect("cart")
        else:
            #add a message that user does not contain order item
            messages.error(request, 'This item was not in your cart')
            return redirect("/products/"+ str(product_id))    
    else:
        #add a message that user does not have an order
        messages.error(request, 'You do not have an active order')
        return redirect("/products/"+ str(product_id))    
    
def checkout(request):
    order = Order.objects.get(user=request.user, ordered=False)
    context = {
            'object':order
    }
    return render(request, 'order/checkout.html',context)

def payment(request):
    order = Order.objects.get(user=request.user, ordered=False)
    order.delete()
    return render(request, 'order/payment.html')