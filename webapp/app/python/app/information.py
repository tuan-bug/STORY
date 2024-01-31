from django.shortcuts import render, get_object_or_404, redirect

from app.models import *
from app.python.app.base import show_manage
def Information(request):
    slide_hidden = "none"
    fixed_height = "20px"
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


    if request.user.is_authenticated:
        user = request.user
        profile = UserProfile.objects.filter(user = user).first()
        address_infor = Adress.objects.filter(customer=user)
    user_address = None
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['adress']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            mobile = form.cleaned_data['mobile']
            user_address = Adress(customer=request.user, adress=address, city=city, state=state, mobile=mobile)
            user_address.save()
    else:
        form = AddressForm()

    if profile:
        print('thông tin profile')
        print(profile.profile_image)
    context = {'user': user,
               'form': form,
               'address_infor': address_infor,
               'user_address': user_address,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'user_not_login': user_not_login,
               'user_login': user_login,
               'items': items,
               'total_all': total_all,
               'count': count,
               'show_manage': show_manage,
               'profile': profile,
               }
    return render(request, 'app/information.html', context)


def edit_information(request):
    slide_hidden = "none"
    fixed_height = "20px"
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

    if request.user.is_authenticated:
        user = request.user
        print(user)

    if request.method == 'POST':
        gender = request.POST.get('gender')
        birthdate = request.POST.get('birthdate')
        profile_image = request.FILES.get('profile_image')
        print(profile_image)
        temp = UserProfile.objects.filter(user=user)
        temp.delete()
        UserProfile.objects.create(
            user=request.user,
            gender=gender,
            birthdate=birthdate,
            profile_image=profile_image,
        )
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("lỗi form")
            print(form.errors)

        return redirect('information')

    form = UserChangeForm(instance=user,
                            initial={
                                'username': user.username,
                                'email': user.email,
                                'last_name': user.last_name,
                                'first_name': user.first_name,
                                })


    context = {'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'user_not_login': user_not_login,
               'user_login': user_login,
               'show_manage': show_manage,
               'items': items,
               'total_all': total_all,
               'count': count,
               'form': form,
               }
    return render(request, 'app/editInformation.html', context)