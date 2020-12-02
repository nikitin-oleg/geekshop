from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from mainapp import views as mainapp
from django.conf.urls.static import static


urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', include('mainapp.urls', namespace='mainapp')),
    path('products/all/', mainapp.products_all, name='products_all'),
    path('products/home/', mainapp.products_home, name='products_home'),
    path('products/office/', mainapp.products_office, name='products_office'),
    path('products/modern/', mainapp.products_modern, name='products_modern'),
    path('products/classic/', mainapp.products_classic, name='products_classic'),
    path('contact/', mainapp.contact, name='contact'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
