from django.shortcuts import render

from app.models import *


def cart(request):
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    slide_hidden = "hidden"
    fixed_height = "20px"
    total_all = 0
    count = 0
    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        user_not_login = "none"
        user_login = "show"
        for item in items:
            print(item)
            item.total = '{:,.0f}'.format(item.product.price * item.quantity)
            total_all += item.product.price * item.quantity
            count += item.quantity
            item.product.price = '{:,.0f}'.format(item.product.price)
    else:
        items = []
        user_not_login = "show"
        user_login = "none"
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    total_all = '{:,.0f}'.format(total_all)
    context = {'items': items,
               'total_all': total_all,
               'count': count,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'categories':categories,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'show_manage': show_manage
               }
    return render(request, 'app/cart.html', context)
