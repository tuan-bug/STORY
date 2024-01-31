from django.shortcuts import render

from app.models import *


def contact(request):
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
            item.total = item.product.price * item.quantity
            total_all += item.product.price * item.quantity
            count += item.quantity
    else:
        items = []
        user_not_login = "show"
        user_login = "none"
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon

    form = FormContact()
    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print('Lỗi khi lưu dữ liệu:', e)
        else:
            print('Dữ liệu không hợp lệ:', form.errors)

    total_all = '{:,.0f}'.format(total_all)
    context ={
        'categories': categories,
        'items': items,
        'total_all': total_all,
        'count': count,
        'user_login': user_login,
        'user_not_login': user_not_login,
        'slide_hidden': slide_hidden,
        'fixed_height': fixed_height,
        'show_manage': show_manage,
        'form': form,
        }
    return render(request, 'app/contact.html', context)

