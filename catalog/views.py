from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    product_list = Category.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\n'
              f'Номер телефона: {phone}\n'
              f'Сообщение: {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def products(request, pk):
    category_of_product = Category.objects.get(pk=pk)
    context = {
        'products': Product.objects.filter(category_of_product=pk),
        'title': f'{category_of_product.name_of_category}'
    }
    return render(request, 'catalog/products.html', context)


def info_about_product(request, pk):
    context = {
        'product': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/info_about_product.html', context)
