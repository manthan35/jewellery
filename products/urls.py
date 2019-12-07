from django.urls import path
from . import views

urlpatterns=[
    path('',views.products,name='products'),
    path('<int:product_id>',views.product,name='product'),
    path('necklaces',views.necklaces,name='necklaces'),
    path('earrings',views.earrings,name='earrings'),
    path('rings',views.rings,name='rings'),
]