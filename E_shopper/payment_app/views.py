from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest,Http404
from order_app.models import OrderModel,OrderItem
from cart_app.models import CartModel,CartItemModel


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def initialize_razorpay(request, order_id):
    order = OrderModel.objects.get(id=order_id)
    user = request.user
    print("intial:",user)
    cart = CartModel.objects.get(user=user)
    cart_items = cart.items.all()
    cart_item = CartItemModel.objects.filter(user=user)

    # print(order)
    order_itemm = OrderItem.objects.filter(order=order)
    # print("order_item: ",order_itemm)
    total_order_amount = order.total_amount
    shipping_cost = 0
    # Initialize Razorpay client with your API keys
    # razorpay_client = razorpay.Client(auth=("your_api_key", "your_secret_key"))

    # Create a Razorpay order
    razorpay_order = razorpay_client.order.create({
        'amount': int(float(order.total_amount) * 100),  # Razorpay expects amount in paise
        'currency': 'INR',
        'payment_capture': 1,  # Auto-capture payment after order creation
    })

    # Save Razorpay order ID in your OrderModel
    order.razorpay_order_id = razorpay_order['id']
    order.status = 'Pending'
    order.save()

    # cart_items.delete()
    # cart_item.delete()
    # Render the Razorpay payment page
    context = {
        'order': order,
        'razorpay_order': razorpay_order,
        'my_order': order,
        'my_order_item_detail' : order_itemm,
        'total_order_amount':total_order_amount,
        'shipping_cost':shipping_cost
    }
    return render(request, 'payment_app/razorpay_payment.html', context)

from django.shortcuts import render
@csrf_exempt
def razorpay_payment_success(request):
    # Update order status or perform other actions
    if request.method == 'POST':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        try:
            order = OrderModel.objects.get(razorpay_order_id=razorpay_order_id)

            # Save the Razorpay details in the order
            order.razorpay_payment_id = razorpay_payment_id
            order.razorpay_order_id = razorpay_order_id
            order.razorpay_signature = razorpay_signature

            # order status make paid
            order.status = 'Paid'
            order.save()
            
            # insure order successs then cart make empty
            user  = order.user
            print("successs: ",user)
            cart = CartModel.objects.get(user=user)
            cart_items = cart.items.all()
            cart_item = CartItemModel.objects.filter(user=user)
            

            cart_items.delete()
            cart_item.delete()
        except OrderModel.DoesNotExist:
            raise Http404("Order does not exist.")
        
    return render(request, 'payment_app/payment_success.html')

