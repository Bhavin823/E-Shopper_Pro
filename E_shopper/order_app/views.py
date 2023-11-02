from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from user_app.models import UserAddress
from cart_app.models import CartModel,CartItemModel
from order_app.models import OrderModel,OrderItem


# Create your views here.
def create_order(request):
    if request.method == 'POST':
        user = request.user
        address_id = request.POST.get('address_id')
        # print("address id:",address_id)
        total_amount = request.POST.get('totalamount')
        # print(total_amount)
        if total_amount is None:
            messages.error(request, 'Cart Has Not Any Items')
            return redirect('cart_app:checkout')
        payment_type  = request.POST.get('PaymentType')
        
        address = UserAddress.objects.get(pk=address_id)
        cart = CartModel.objects.get(user=user)
        cart_items = cart.items.all()
        # print("cart items during cart items: ",cart_items)
        
        order = OrderModel.objects.create(
            user = user,
            shipping_address = address,
            payment_type = payment_type,
            total_amount = total_amount,
        )
        # order.ordered_items.set(cart_items)
        cart_item = CartItemModel.objects.filter(user=user)
        for item in cart_item:
            price = item.product.ProductPrice * item.quantity
            OrderItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                price = price,
            )

        if payment_type == 'Cash On Delivary':
            order.status = 'Pending'
            order.save()
        elif payment_type == 'Online':
            order.status = 'Paid'
            order.save()

        cart_items.delete()
        cart_item.delete()

        response_data = {
                'message': 'Order successfully created',
                'selected_address_id': address_id,
                'totalamount':total_amount,
                'payment_type': payment_type,
            }
   

    return JsonResponse(response_data)

def order_detail(request,id):
    order= OrderModel.objects.get(id=id)
    # print(order)
    order_itemm = OrderItem.objects.filter(order=order)
    # print("order_item: ",order_itemm)
    total_order_amount = order.total_amount
    shipping_cost = 0

    context = {
        'my_order': order,
        'my_order_item_detail' : order_itemm,
        'total_order_amount':total_order_amount,
        'shipping_cost':shipping_cost
    }
    return render(request,'order_app/order_detail.html',context)

