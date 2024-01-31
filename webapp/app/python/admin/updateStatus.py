from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import *

@csrf_exempt
def update_status(request):
    if request.method == 'POST':
        slide_id = request.POST.get('slide_id')
        try:
            slide = Slide.objects.get(id=slide_id)
            print(slide)
            slide.status = 0
            slide.save()
            return JsonResponse({'message': 'Cập nhật thành công'})
        except Slide.DoesNotExist:
            return JsonResponse({'message': 'Slide không tồn tại'}, status=404)

    return JsonResponse({'message': 'Invalid method'}, status=405)
