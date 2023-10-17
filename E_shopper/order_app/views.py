from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from user_app.models import UserAddress,UserProfile
from cart_app.models import CartModel,CartItemModel
from order_app.models import OrderModel

# Create your views here.
def create_order(request):
    if request.method == 'POST':
        user = request.user
        address_id = request.POST.get('address_id')
        print("address id:",address_id)
        total_amount = request.POST.get('totalamount')
        print(total_amount)
        if total_amount is None:
            messages.error(request, 'Cart Has Not Any Items')
            return redirect('cart_app:checkout')
        payment_type  = request.POST.get('PaymentType')
        
        address = UserAddress.objects.get(pk=address_id)
        cart = CartModel.objects.get(user=user)
        cart_items = cart.items.all()

        order = OrderModel.objects.create(
            user = user,
            shipping_address = address,
            payment_type = payment_type,
            total_amount = total_amount,
        )

        if payment_type == 'Cash On Delivary':
            order.status = 'Pending'
            order.save()
        elif payment_type == 'Online':
            order.status = 'Paid'
            order.save()

        cart_items.delete()

        response_data = {
                'message': 'Order successfully created',
                'selected_address_id': address_id,
                'totalamount':total_amount,
                'payment_type': payment_type,
            }
   

    return JsonResponse(response_data)
    