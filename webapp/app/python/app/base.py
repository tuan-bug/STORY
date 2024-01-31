from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import *


def base(request):
    user = request.user
    if user.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    slide = Slide.objects.all()
    test = slide.category_slide
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    context = {
        'slide': slide,
        'categories': categories,
        'show_manage': show_manage,
    }
    return render(request, 'app/base.html', context)

def getHome(request):
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "none"


    storys = Story.objects.all()
    print(storys)

    context = {
        'storys': storys,
        'user_not_login': user_not_login,
        'user_login': user_login,
    }
    return render(request, 'app/home.html', context)


def show_manage(request):
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'

    return show_manage
