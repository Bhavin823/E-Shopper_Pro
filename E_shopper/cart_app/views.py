from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product_app.models import ProductModel
from cart_app.models import CartItemModel,CartModel
from user_app.models import UserProfile ,UserAddress


# Create your views here.

# this function work for specified subcategory product page,all product page,productdetail page
@login_required
def add_to_cart(request,productslug):
    user = request.user
    product = ProductModel.objects.get(slug=productslug)
    # print(product)

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
    if not cart_item_exist:
        cart_item = CartItemModel.objects.create(user=user, product=product)
        cart.items.add(cart_item)
    
    subcatslug = request.GET.get('subcatslug', '')
    # print("subcatslug",subcatslug)
    
    # if product add on cart from all product page
    if subcatslug == "all":
        # redirect to all product page after add product to cart
        return redirect('product_app:products',subcatslug=subcatslug)
    # if product add on cart from productdetail page
    elif subcatslug == "productdetail":       
        # redirect to productdetail page after add product to cart
        return redirect('product_app:productdetail',productslug=productslug)
    # if product add on cart from subcategory wise product page
    else:
        # redirect to subcategory wise product page after add product to cart
        return redirect('product_app:products',subcatslug=subcatslug)

# show cart view with image,name,quantity ,subtotal
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

# delete specified cart item
def delete_cart_item(request, item_id):
    retpath = request.GET.get('retpath', '')
    try:
        cart_item = CartItemModel.objects.get(id=item_id)
        cart_item.delete()
    except CartItemModel.DoesNotExist:
        # Handle the case where the item doesn't exist
        pass
    if retpath == "checkout":
        return redirect('cart_app:checkout')
    return redirect('cart_app:cart')

# delte whole cart 
def clear_cart(request):
    retpath = request.GET.get('retpath', '')
    # Delete all cart items for the current user
    CartItemModel.objects.filter(user=request.user).delete()
    if retpath == "checkout":
        return redirect('cart_app:checkout')
    # Redirect back to the cart
    return redirect('cart_app:cart')

# increment item quantity
@login_required
def increment_cart_quantity(request,item_id):
    retpath = request.GET.get('retpath', '')
    try:
        cart_item = CartItemModel.objects.get(id=item_id,user=request.user)
        cart_item.quantity +=1
        cart_item.save()
    except CartItemModel.DoesNotExist:
        pass

    if retpath == "checkout":
        return redirect('cart_app:checkout')
    return redirect('cart_app:cart')

# decrement item quantity
@login_required
def decrement_cart_quantity(request, item_id):
    retpath = request.GET.get('retpath', '')
    try:
        cart_item = CartItemModel.objects.get(id=item_id, user=request.user)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
    except CartItemModel.DoesNotExist:
        pass

    if retpath == "checkout":
        return redirect('cart_app:checkout')
    return redirect('cart_app:cart')

# checkout view
@login_required
def checkoutView(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    user_addresses = UserAddress.objects.filter(user=user)
    cart = CartModel.objects.get(user=user)
    cart_item = cart.items.all()
    cart_total = sum(item.subtotal() for item in cart_item)
    shipping_cost = 0
    # retpath = request.POST.get('retpath', '')
    # selected_address_id = request.POST.get('selected_address')
    selected_address_id = request.GET.get('selected_address')
    # print("selected_address_id: ",selected_address_id)
    context = {
        'cart_items':cart_item,
        'cart': cart,
        'cart_total':cart_total,
        'shipping_cost':shipping_cost,
        'user_profile':user_profile,
        'user_addresses': user_addresses,
        'selected_address_id':selected_address_id,
    }
    
    return render(request, 'cart_app/checkout.html', context)



