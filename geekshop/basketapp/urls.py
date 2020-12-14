from django.urls import path, include
from basketapp import views as basketapp


app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='basket'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('delete/<int:pk>/', basketapp.basket_remove, name='delete'),
    path('remove/ajax/<int:pk>/', basketapp.basket_remove_ajax, name='remove_ajax'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit'),
]