from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt

from app.models import *
from app.python.admin.manage import is_admin
@login_required
@user_passes_test(is_admin)
def manageSlide(request):
    feedback = Contact.objects.all().count()
    contacts = Contact.objects.all()
    slides = Slide.objects.all()
    categories = Category.objects.all()
    form = AddSlide()
    context ={'feedback': feedback,
              'contacts': contacts,
              'slides': slides,
              'form': form,
              'categories': categories,
              }
    return render(request, 'admin/managementSlide.html', context)

def addSlide(request):
    form = AddSlide()
    if request.method == 'POST':
        form = AddSlide(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm slide thành công')
            return redirect('manageSlide')
        else:
            messages.error(request, 'Thêm slide thất bại')
    else:
        messages.error(request, 'Thêm slide thất bại')

    # if request.method == 'POST':
    #     form = AddSlide(request.POST, request.FILES)
    #     if form.is_valid():
    #         # Lưu dữ liệu vào CSDL
    #         slide = form.save()
    #         return JsonResponse({'success': 'Slide đã được thêm thành công.'})
    #     else:
    #         return JsonResponse({'error': form.errors}, status=400)
    # return JsonResponse({'error': 'Yêu cầu không hợp lệ.'}, status=400)

    context = {'form': form,
               'messages': messages,
               }
    return render(request, 'admin/addSlide.html', context)


def get_slide(request, slide_id):
    slide = get_object_or_404(Slide, id=slide_id)
    data = {
        'category_slide': slide.category_slide,
        'name': slide.name,
        # Thêm các trường khác nếu cần
    }
    return JsonResponse(data)
def editSlide(request, slide_id):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    slide = get_object_or_404(Slide, id=slide_id)
    if request.method == 'POST':
        form = Slide(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa slide thành công!!')
            return redirect('manageSlide')
        else:
            messages.error(request, 'Sửa slide thất bại')
    else:
        messages.error(request, 'Sửa slide thất bại')

    form = AddSlide(instance=slide,
                       initial={'category_slide': slide.category_slide,
                                'name': slide.name,
                                'image': slide.image,
                                })

    print(form.initial.items())
    context = {'slide': slide,
               'form': form}
    return render(request, 'admin/editSlide.html', context)


def deleteSlide(request, id):
    # id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    slide = get_object_or_404(Slide, id=id)
    Slide.objects.filter(id=id).delete()
    messages.success(request, 'Xóa slide thành công ')
    return redirect('manageSlide')
    context ={'slide': slide,
              'messages': messages,}
    return render(request, 'admin/deleteSlide.html', context)

@csrf_exempt
def edit_status(request):
    if request.method == 'POST':
        slide_id = request.POST.get('slide_id')
        try:
            slide = Slide.objects.get(pk=slide_id)
            slide.status = 0
            slide.save()
            return JsonResponse({'message': 'Cập nhật thành công'})
        except Slide.DoesNotExist:
            return JsonResponse({'message': 'Slide không tồn tại'}, status=404)

    return JsonResponse({'message': 'Invalid method'}, status=405)