from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from products.models import Product
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    product_name = product.name.upper()

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, (
            f'Updated {product_name} '
            f'quantity to {cart[item_id]}'))
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product_name} to your cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """Update the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    product_name = product.name.upper()

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, (
            f'Updated {product_name} '
            f'quantity to {cart[item_id]}'))
    else:
        cart.pop(item_id)
        messages.success(request, (
            f'Removed {product_name} '
            f'from your cart'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

# remove csrf protection to delete items from the cart


@require_POST
@csrf_exempt
def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=item_id)
    product_name = product.name.upper()

    if item_id in list(cart):

        try:
            cart.pop(item_id)
            messages.success(request, f'Removed {product_name} from your cart')

            request.session['cart'] = cart
            return HttpResponse(status=200)

        except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)
