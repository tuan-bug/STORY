from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def loginPage(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    user_not_login = "show"
    user_login = "none"
    if request.user.is_authenticated: # neu da xac thuc
        return redirect('home')
    if request.method == 'POST':
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        user = authenticate(request, username=userName, password=passWord)
        if user is not None:
            login(request, user)
            messages.success(request, 'Đăng nhập thành công.')
            print(user.is_staff)
            if user.is_staff:
                return redirect('home_manage')
            return redirect('home')
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không chính xác')
    context = {'user_login': user_login,
               'user_not_login': user_not_login,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,}
    return render(request, "app/login.html", context)

def logoutPage(request):
    logout(request)
    return redirect('login')

