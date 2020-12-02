from django.shortcuts import render
import datetime
from .models import ProductCategory, Product, LinksMenu, Contacts


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)
    title = 'продукты'
    links_menu = LinksMenu.objects.all()
    # same_products = SameProducts.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        # 'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


# def contact(request):
#     content = {
#         'title': 'Контакты',
#     }
#     return render(request, 'mainapp/contact.html', content)


def products_all(request):
    title = 'продукты'
    links_menu = LinksMenu.objects.all()
    # same_products = SameProducts.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        # 'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def products_home(request):
    title = 'продукты'
    links_menu = LinksMenu.objects.all()
    # same_products = SameProducts.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        # 'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def products_office(request):
    title = 'продукты'
    links_menu = LinksMenu.objects.all()
    # same_products = SameProducts.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        # 'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def products_modern(request):
    title = 'продукты'
    links_menu = LinksMenu.objects.all()
    # same_products = SameProducts.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        # 'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def products_classic(request):
    title = 'продукты'
    links_menu = LinksMenu.objects.all()
    # same_products = SameProducts.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        # 'same_products': same_products
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
    }
    return render(request, 'mainapp/contact.html', content)
