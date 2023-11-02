from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_in = request.GET.get('sort', None)
    phones = Phone.objects.all()
    if sort_in == 'name':
        phones = Phone.objects.all().order_by(sort_in)
    elif sort_in == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_in == 'max_price':
        phones = Phone.objects.all().order_by('price')
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        "phone": phone
    }
    return render(request, template, context)
