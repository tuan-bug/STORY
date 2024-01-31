from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *

from django.contrib.auth.decorators import login_required, user_passes_test

from app.python.admin.manage import is_admin
@login_required
@user_passes_test(is_admin)
def manageCategory(request):
    categories = Category.objects.all().order_by('name')  # lay cac damh muc lon
    paginator = Paginator(categories, 6)
    page_number = request.GET.get('page')
    page_categories = paginator.get_page(page_number)
    feedback = Contact.objects.all().count()
    contacts = Contact.objects.all()
    context ={'categories': page_categories,
              'feedback': feedback,
              'contacts': contacts,
              }
    return render(request, 'admin/managementCategory.html', context)
def addCategory(request):
    form = AddCategory()
    if request.method == 'POST':
        form = AddCategory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm danh mục thành công')
            return redirect('manageCategory')
        else:
            messages.error(request, 'Thêm danh mục thất bại')
    else:
        messages.error(request, 'Thêm danh mục thất bại')
    context = {'form': form,
               'messages': messages,
               }
    return render(request, 'admin/addCategory.html', context)

def editCategory(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = AddCategory(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa danh mục thành công')
            return redirect('manageCategory')
        else:
            messages.success(request, 'Sửa danh mục thất bại')
    else:
        messages.success(request, 'Sửa danh mục thất bại')
    form = AddCategory(instance=category,
                       initial={'sub_category': category.sub_category,
                                'is_sub': category.is_sub,
                                'name': category.name,
                                'slug': category.slug,
                                'image': category.image,
                                'messages': messages,
                                })

    context = {'category': category,
               'form': form}
    return render(request, 'admin/editCategory.html', context)


def deleteCategory(request, id):
    # id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    category = get_object_or_404(Category, id=id)
    Category.objects.filter(id=id).delete()
    messages.success(request, 'Đã xóa danh mục')
    return redirect('manageCategory')
    context ={'category': category,
              'messages': messages,}
    return render(request, 'admin/deleteCategory.html', context)