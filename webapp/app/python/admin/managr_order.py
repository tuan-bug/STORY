from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from app.models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from app.python.admin.manage import is_admin
@login_required
@user_passes_test(is_admin)
def manageOrder(request):
    feedback = Contact.objects.all().count()
    contacts = Contact.objects.all()
    orders = Order.objects.all()
    order_check = {}
    order_price = {}
    for order in orders:
        order_price[order.id] = '{:,.0f}'.format(order.get_cart_total)
        check = PaymentRecord.objects.filter(order_id=order.id).exists()
        print("Check test xem sao: ")
        print(check)
        order_check[order.id] = check
        print(order_check)

    context = {
        'orders': orders,
        'order_price': order_price,
        'order_check': order_check,
        'feedback': feedback,
        'contacts': contacts,

    }
    return render(request, 'admin/manageOrders.html', context)

def viewOrder(request):
    id = request.GET.get('id', '')
    order =  get_object_or_404(Order, id=id)
    print('id order: ')
    print(id)
    order_items = {}
    total = 0
    items = OrderItem.objects.filter(order=order)
    order_items[order] = items
    total_order_amount = 0
    for item in items:
        total += item.total

    total = '{:,.0f}'.format(total)
    print(total)
    context={'order': order,
             'order_items': order_items,
             'items': items,
             'total': total,
             }
    return render(request, 'admin/view_order.html', context)

def delOrder(request, id):
    order = get_object_or_404(Order, id=id)
    print(order)
    Order.objects.filter(id=id).delete()
    messages.success(request, 'Xóa đơn hàng thành công')
    return redirect('manageOrder')

    context = {'product': order}

    return render(request, 'admin/delete_order.html', context)