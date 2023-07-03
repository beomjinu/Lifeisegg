from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from app.shop.views import redirect_index

from app.shop.sitemaps import ProductSitemap
from app.terms.sitemaps import TermsSitemap

sitemaps = {
    'Product': ProductSitemap,
    'Trems': TermsSitemap, 
}

urlpatterns = [
    # admin
    path('adminpage/', admin.site.urls),
    
    # apps
    path('shop/', include("app.shop.urls")),
    path('', redirect_index), # redirect shop/
    path('terms/', include("app.terms.urls")),
    path('order/', include("app.order.urls")),
    path('payment/', include('app.payment.urls')),
    path('cart/', include('app.cart.urls')),
    path('nimda/', include('app.nimda.urls')), # new admin
    
    # sitemaps
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
