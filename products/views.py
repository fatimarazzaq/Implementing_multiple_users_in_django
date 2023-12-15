from django.http import JsonResponse
from django.shortcuts import render
from .models import Product,Order,OrderItem,Buyer
from django.contrib.auth.decorators import login_required
import json

# Create your views here.


def store(request):
    if request.user.is_authenticated:
        buyer=request.user.buyer
        order,created=Order.objects.get_or_create(buyer=buyer,complete=False)
        cartitems=order.order_item_quantity
    else:
        orderitem=[]
        order={
            'order_item_total':0,
            'order_item_quantity':0,
            'order_item_quantity':0,
        }
    all_products=Product.objects.all()
    return render(request,'products/store.html',{'all_products':all_products,'cartitems':cartitems})


@login_required
def cart(request):
    if request.user.is_authenticated:
        try:
            buyer=request.user.buyer
            order,created=Order.objects.get_or_create(buyer=buyer,complete=False)
            orderitem=order.orderitem_set.all()
            cartitems=order.order_item_quantity
        except :
            # buyer=Buyer(user=request.user,buyer_name=request.user.username,buyer_email=request.user.email)
            # buyer.save()
            # order=Order.objects.create(buyer=buyer,complete=False)
            # # created.save()
            # orderitem=OrderItem.objects.create()
            pass
    else:
        orderitem=[]
        # order={
        #     'order_item_total':0,
        #     'order_item_quantity':0,
        # }
    context={
        'orderitem':orderitem,
        'order':order,
        'cartitems':cartitems,
    }
    return render(request,'products/cart.html',context)



@login_required
def checkout(request):
    if request.user.is_authenticated:
        buyer=request.user.buyer
        order,created=Order.objects.get_or_create(buyer=buyer,complete=False)
        orderitem=order.orderitem_set.all()
        cartitems=order.order_item_quantity
        
    else:
        orderitem=[]
        # order={
        #     'order_item_total':0,
        #     'order_item_quantity':0,
        # }
    context={
        'orderitem':orderitem,
        'order':order,
        'cartitems':cartitems,
    }
    return render(request,'products/checkout.html',context)



def updateItem(request):
    data=json.loads(request.body)
    product_id=data['productId']
    action=data['action']
    product=Product.objects.get(id=product_id)
    buyer=request.user.buyer
    order,created=Order.objects.get_or_create(buyer=buyer,complete=False)
    orderitem,created=OrderItem.objects.get_or_create(product=product,order=order)
    if action=='add':
        orderitem.quantity+=1
    elif action=='remove':
        orderitem.quantity-=1

    orderitem.save()
    if orderitem.quantity<=0:
        orderitem.delete()
    return JsonResponse('This is update item',safe=False)