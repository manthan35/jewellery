from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('pages.urls')),
    path('products/',include('products.urls')),
    path('accounts/',include('accounts.urls')),
    path('order/',include('order.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
