from django.shortcuts import render

from app.models import *
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def homeManage(request):
    orders = Order.objects.all();
    count = 0;
    total_2 = 0
    for order in orders:
        if order:
            count += 1
            total_2 += order.get_cart_total

    items = OrderItem.objects.all()

    total = 0
    for item in items:
        if item:
            total += item.total
            print("tien: ")
            print(total)

    users = User.objects.all()
    member = 0
    for user in users:
        if user:
            member += 1

    feedback = Contact.objects.all().count()
    contacts = Contact.objects.all()
    total_2 = '{:,.0f}'.format(total_2)
    context = {
        'count': count,
        'total': total_2,
        'member': member - 1,
        'feedback': feedback,
        'contacts': contacts,
    }
    return render(request, 'admin/home_manage.html', context)