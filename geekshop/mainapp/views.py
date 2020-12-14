from django.shortcuts import render
import datetime
from .models import ProductCategory, Product, Contacts
from django.shortcuts import get_object_or_404
import random

from basketapp.models import Basket


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products_list = Product.objects.all()

    return random.sample(list(products_list), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category__pk=hot_product.category.pk).exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products, 'basket': get_basket(request.user),}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)


    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category = {'name': 'все', 'pk': 0}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)

        content = {
            'title': title,
            'links_menu': links_menu,
            'products_list': products_list,
            'category': category,
            'basket': get_basket(request.user),
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    locations = Contacts.objects.all()
    content = {
        'title': title,
        'visit_date': visit_date,
        'locations': locations,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)
