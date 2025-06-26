from django.shortcuts import render
from .models import Product, Tag

def product_list(request):
    tag_name = request.GET.get('tag')
    if tag_name:
        products = Product.objects.filter(tag__name=tag_name)
    else:
        products = Product.objects.all()
    tags = Tag.objects.all()
    return render(request, 'gadjets/product_list.html', {
        'products': products,
        'tags': tags,
        'selected_tag': tag_name
    })