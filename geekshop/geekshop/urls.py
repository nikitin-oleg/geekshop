from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from mainapp import views as mainapp
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include



urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('contact/', mainapp.contact, name='contact'),
    path('basket/', include('basketapp.urls', namespace='basket')),
    # path('admin/', admin.site.urls),
    path('admin/', include('adminapp.urls', namespace='admin'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
