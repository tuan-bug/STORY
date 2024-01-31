from django.shortcuts import render

from app.models import *


def information_address(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    # check xem phải admin không
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'

    total_all = 0
    count = 0
    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        user_not_login = "none"
        user_login = "show"
        for item in items:
            print(item)
            item.total = item.product.price * item.quantity
            total_all += item.product.price * item.quantity
            count += item.quantity
    else:
        items = []
        user_not_login = "show"
        user_login = "none"
    total_all = '{:,.0f}'.format(total_all)
    print('hihihh: ')
    print(user_login, user_not_login)
    # XỬ LÝ CHÍNH
    address_infor = Adress.objects.filter(customer=request.user)
    if request.user.is_authenticated:
        user = request.user

    form = AddressForm()
    context = {'address_infor': address_infor,
               'fixed_height': fixed_height,
               'slide_hidden': slide_hidden,
               'form': form,
               'show_manage': show_manage,
               'user_not_login': user_not_login,
               'user_login': user_login,
               'count': count,
               'items': items,
               'total_all': total_all,
               }
    return render(request, 'app/information_address.html', context)
