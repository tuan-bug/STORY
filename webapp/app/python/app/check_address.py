from django.contrib import messages
from django.shortcuts import render, redirect

from app.models import *


def Continue1(request):

    slide_hidden = "hidden"
    fixed_height = "20px"
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    # lấy các sản phẩm
    total_all = 0
    count = 0
    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        user_not_login = "none"
        user_login = "show"
        for item in items:
            item.total = item.product.price * item.quantity
            total_all += item.product.price * item.quantity
            count += item.quantity
    else:
        order = None
        items = []
        user_not_login = "show"
        user_login = "none"
    # total_all = '{:,.0f}'.format(total_all)
    total_temp = total_all

# Xử lý chính
    id = request.GET.get('id', '')
    print("lấy id của address: " + id)
    payment_method_value = request.GET.get('payment_method', '')
    print("Phương thức thanh toán:", payment_method_value)
    address = Adress.objects.filter(id=id)
    address_data = address.values()
    try:
        single_address = address.get()
        # Lấy các trường cụ thể, ví dụ lấy tên người dùng và địa chỉ
        city = single_address.city
        address_sate = single_address.adress
        name = single_address.name_user
        mobile = single_address.mobile
        district = single_address.district
        commune = single_address.commune
        order = Order(customer=customer, address=single_address, complete=False)
        order.save()

        for item in items:
            items_order = OrderItem(product=item.product, order=order, quantity=item.quantity, total= item.product.price * item.quantity)
            items_order.save()
            items_order.product.count -= item.quantity
            items_order.product.sell_number += item.quantity
            item.product.save()
            print("Lưu thành công đối tượng OrderItem, SL còn: ")
            print(items_order.product.count)

        products = OrderItem.objects.filter(order=order)
        for item in products:
            item.total = item.product.price * item.quantity

        items.delete()
    except Adress.DoesNotExist:
        # Xử lý trường hợp không tìm thấy bản ghi
        pass
    print(name, city, address_sate, mobile, district, commune)
    for item in items:
        print(item)

    print('Tien: ')
    print(total_temp)
    if payment_method_value == 'credit_card':
        # Điều hướng đến trang thanh toán trực tuyến (thay thế URL này bằng URL thực tế của bạn)
        return render(request, 'payment/payment.html', {'total_amount': total_temp,
                                                        'order_id': order.id,
                                                        } )
    context = {
               'products': products,
               'total_all': total_all,
               'count': count,
               'user_login': user_login,
               'user_not_login': user_not_login,

               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'show_manage': show_manage
               }
    return render(request, 'app/address.html', context)
