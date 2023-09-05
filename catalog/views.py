from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, CreateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version


class HomeListView(ListView):
    model = Category
    template_name = 'catalog/home.html'


class ContactView(View):
    def get(self, request):
        context = {
            'title': 'Контакты'
        }
        return render(request, 'catalog/contacts.html', context)

    def post(self, request):
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


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_of_product=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        category_item = Category.objects.get(pk=self.kwargs['pk'])
        context_data['title'] = category_item.name_of_category

        for product in context_data['products']:
            version = product.version_set.first()
            product.version = version

        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/info_about_product.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:home')
