from django.urls import path
from . import views

urlpatterns = [
    path(' ',views.cart,name='cart'),
    path('<int:product_id>',views.add_to_cart,name='add-to-cart'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove-from-cart'),
    path('remove_singal_item_from_cart/<int:product_id>',views.remove_singal_item_from_cart,name='remove-singal-item-from-cart'),
    path('checkout',views.checkout,name='checkout'),
    path('payment',views.payment,name='payment'),
]
