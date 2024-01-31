from django.shortcuts import get_object_or_404, render

from app.models import *


def detail(request):

    id = request.GET.get('id', '') # lấy id khi người dùng vlick vào sản phẩm nào đó
    story = Story.objects.get(id=id)
    print(story.id)
    chapters = Chapter.objects.filter(story=story)
    context = {
        'story': story,
        'chapters': chapters
    }
    return render(request, 'app/detail.html', context)
