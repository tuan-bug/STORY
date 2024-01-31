from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *


def myOrder(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    show_manage = 'show'  # Đảm bảo rằng biến show_manage đã được khai báo

    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        user_not_login = "none"
        user_login = "show"
        for item in items:
            print(item)
            # item.total = item.product.price * item.quantity
            # total_all += item.product.price * item.quantity
            # count += item.quantity
    else:
        items = []
        user_not_login = "show"
        user_login = "none"


    my_orders = Order.objects.filter(customer=request.user)
    order_items = {}  # Tạo một từ điển để lưu trữ các đơn hàng và mặt hàng tương ứng
    order_addresses = {}  # Tạo một từ điển để lưu trữ đơn hàng và thông tin địa chỉ tương ứng
    order_total_amounts = {}
    order_check = {}
    for order in my_orders:
        items = OrderItem.objects.filter(order=order)
        order_items[order] = items
        total_order_amount = 0
        for item in items:
            total_order_amount += item.total
            print("tong gia order : ")
            print(total_order_amount)
        order_total_amounts[order.id] = total_order_amount

        address = order.address  # Truy cập vào đối tượng Address liên kết với đơn hàng
        order_addresses[order] = address
        print("ID")
        print(order.id)
        check = PaymentRecord.objects.filter(order_id=order.id)
        print("Check test xem sao: ")
        print(check)
        order_check[order.id] = check
        print(order_check)
        if order.id in order_total_amounts:  # Sửa lại kiểm tra xem order.id có trong order_total_amounts
            print(f"Giá trị đã được lưu cho đơn hàng '{order}': {order_total_amounts[order.id]}")
        else:
            print(f"Không tìm thấy giá trị cho đơn hàng '{order}' trong order_total_amounts.")

    order_total_amounts_list = [(order_id, total_amount) for order_id, total_amount in order_total_amounts.items()]  # Đặt danh sách ngoài vòng lặp

    context = {
        'order_addresses': order_addresses,
        'user_not_login': user_not_login,
        'user_login': user_login,
        'order_check': order_check,
        'order_items': order_items,
        'slide_hidden': slide_hidden,
        'fixed_height': fixed_height,
        'show_manage': show_manage,
        'my_order': my_orders,
        'order_total_amounts': order_total_amounts,
        'order_total_amounts_list': order_total_amounts_list,  # Đưa vào context
    }
    return render(request, 'app/my_order.html', context)


def deletemyOrder(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    order = get_object_or_404(Order, id=id)
    print(order)
    items = OrderItem.objects.filter(order=order)
    print(items)
    if request.method == 'POST':
        items.delete()
        order.delete()
        messages.success(request, 'Xóa đơn hàng thành công')
        return redirect('myOrder')
    context = {'product': order}

    return render(request, 'app/delete_my_order.html', context)
