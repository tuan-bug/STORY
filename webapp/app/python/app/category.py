from django.shortcuts import render

from app.models import *
from django.db.models import Q


def category(request):
    slide_hidden = "hidden"
    fixed_height = "20px"

    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    categories = Category.objects.filter(is_sub=False) #lay cac damh muc lon

    active_category = request.GET.get('category', '')
    # Lấy danh mục cha
    category = Category.objects.get(slug=active_category)

    # Xây dựng truy vấn Q để lấy tất cả sản phẩm trong danh mục cha và tất cả danh mục con của nó
    query = Q(category=category) | Q(category__sub_category=category)

    # Thực hiện truy vấn để lấy tất cả sản phẩm thuộc danh mục cha và danh mục con
    products = Product.objects.filter(query)
    sub_categories = category.sub_categories.all()

    print("Category:", category.name)
    print("Sub-Categories:")
    for sub_category in sub_categories:
        print(sub_category.name)
    print("Category:", category.name)
    print("Products:")
    print(products)
    print("/// hết")

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
    context ={'items': items,
              'total_all': total_all,
              'count': count,
              'categories': categories,
              'products': products,
              'category': category,
              'sub_categories': sub_categories,
              'active_category': active_category,
              'user_login': user_login,
              'user_not_login': user_not_login,
              'slide_hidden': slide_hidden,
              'fixed_height': fixed_height,
              'show_manage': show_manage,
              }
    return render(request, "app/category.html", context)
