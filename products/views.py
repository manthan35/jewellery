from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Product
def products(request):   
    products = Product.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context ={
                'products' :paged_products
    }
    return render(request, 'products/products.html',context)

def product(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    context ={
        'product' : product
    }
    return render(request,'products/product.html',context)

def necklaces(request):
    products = Product.objects.order_by('-list_date').filter(type='Necklace')
    context = {
        'products' :products
    }
    return render(request, 'products/necklaces.html',context)

def earrings(request):
    products = Product.objects.order_by('-list_date').filter(type='Earring')
    context = {
        'products' :products
    }
    return render(request, 'products/earrings.html',context)

def rings(request):
    products = Product.objects.order_by('-list_date').filter(type='Ring')
    context = {
        'products' :products
    }
    return render(request, 'products/rings.html',context)