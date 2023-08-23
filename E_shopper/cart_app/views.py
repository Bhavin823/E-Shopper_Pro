from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from product_app.models import ProductModel
from cart_app.models import CartItemModel,CartModel
from category_app.models import SubCategoryModel
from django.http import JsonResponse,HttpResponse


# Create your views here.

@login_required
def add_to_cart(request,productdetailslug):
    user = request.user
    product = ProductModel.objects.get(slug=productdetailslug)
    print(product)

    # Find the user's cart or create a new one
    try:
        cart = CartModel.objects.get(user=user)
    except CartModel.DoesNotExist:
        cart = CartModel.objects.create(user=user)

    # Check if the cart item already exists for the product
    try:
        cart_item = CartItemModel.objects.get(user=user, product=product)
        cart_item_exist = True
    except CartItemModel.DoesNotExist:
        cart_item_exist = False

    # If the cart item exists, increase its quantity; otherwise, create it
    if cart_item_exist:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItemModel.objects.create(user=user, product=product)
        cart.items.add(cart_item)
    
    # subcategoryslug = get_object_or_404(SubCategoryModel, slug=productslug)
    # subcategoryslug = get_object_or_404(SubCategoryModel, slug=productslug) #fetch slug of specified product
    # products  = ProductModel.objects.filter(subcategory=subcategoryslug)
    # product = ProductModel.objects.get(slug=productdetailslug)
    # print(subcategoryslug)
    # return redirect('product_app:products',productslug) 
    return HttpResponse("add_to_cart")

@login_required
def cartView(request):
    user = request.user

    try:
        cart = CartModel.objects.get(user=user)
    except CartModel.DoesNotExist:
        cart = CartModel.objects.create(user=user)
    
    cart_item = cart.items.all()
    # print(cart_item)

    cart_total = sum(item.subtotal() for item in cart_item)
    # print(total_price)
    shipping_cost = 0
    context = {
        'cart_items':cart_item,
        'cart': cart,
        'cart_total':cart_total,
        'shipping_cost':shipping_cost
    }

    return render(request,'cart_app/cart.html',context)

def delete_cart_item(request, item_id):
    
    try:
        cart_item = CartItemModel.objects.get(id=item_id)
        cart_item.delete()
    except CartItemModel.DoesNotExist:
        # Handle the case where the item doesn't exist
        pass

    # Find the cart item
    # cart_item = CartItemModel.objects.get(id=item_id)
    
    # # Delete the cart item 
    # cart_item.delete()

    return redirect('cart_app:cart')

def clear_cart(request):

    # Delete all cart items for the current user
    CartItemModel.objects.filter(user=request.user).delete()

    # Redirect back to the cart
    return redirect('cart_app:cart')