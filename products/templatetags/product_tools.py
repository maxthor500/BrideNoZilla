from django import template

register = template.Library()


@register.filter(name='products_showed')
def products_showed(products):
    products_showed = []
    for product in products:
        if product.category.name != "cakes":
            products_showed.append(product)
    return products_showed
