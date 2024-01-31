from django.shortcuts import render

from app.models import *


def searchProduct(request):
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
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
    if request.user.is_authenticated: # neu da xac thuc
        user_not_login = "none"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "none"

    if request.method == "POST":
        search = request.POST["searched"]
        keys = Product.objects.filter(name__contains=search)
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
            order = None
            items = []
        total_all = '{:,.0f}'.format(total_all)
    return render(request, "app/search.html",
                  {'categories': categories,
                   'items': items,
                   'total_all': total_all,
                   'count': count,
                   'user_login': user_login,
                   'user_not_login': user_not_login,
                   "search": search,
                   "keys": keys,
                   'items': items,

                   'slide_hidden': slide_hidden,
                   'fixed_height': fixed_height,
                   'show_manage': show_manage,
                   })
