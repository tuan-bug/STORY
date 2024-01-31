from django.shortcuts import render

from django.contrib.auth.decorators import login_required, user_passes_test

from app.models import Contact


def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def Manage(request):
    feedback = Contact.objects.all().count()
    contacts = Contact.objects.all()

    context ={'feedback': feedback,
              'contacts': contacts,

              }
    return render(request, 'admin/manage.html', context)
