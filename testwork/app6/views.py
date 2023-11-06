from django.shortcuts import render
from django.db.models import Sum
from app5.models import Product


def total_in_db(request):                                    # 3.49 - большое время 
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
    'title': 'Общее количество посчитано в базе данных',
    'total': total,
    }
    return render(request, 'total_count.html', context)


def total_in_view(request):                                  # 0.93 - оптимал 
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
    'title': 'Общее количество посчитано в представлении',
    'total': total,
    }
    return render(request, 'total_count.html', context)


def total_in_template(request):                              # 0.71 - так делать не надо, нарушена схема MVT
    context = {
    'title': 'Общее количество посчитано в шаблоне',
    'products': Product,
    }
    return render(request, 'total_count.html', context)

