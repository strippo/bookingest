import datetime
from django import template
from pdz.warehouse.models import Product

register = template.Library()


@register.inclusion_tag('warehouse/templatetags/product_homebox.html', takes_context=True)
def product_homebox(context):
    products = Product.objects.all()
    context['products_number'] = products.count()
    context['products_available'] = 0
    context['products_to_recharge'] = 0
    context['products_over'] = 0
    for product in products: 
        available_quantity = product.get_available_quantity()
        context['products_available'] += available_quantity
        if available_quantity > 0 and available_quantity < 5:
            context['products_to_recharge'] += 1
        if available_quantity == 0:
            context['products_over'] += 1
    return context
