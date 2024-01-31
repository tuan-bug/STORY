from rest_framework import generics

from app.models import *
from app.serializers import CategoryAPI


class CreateCategoryAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAPI

class UpdateCategoryAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAPI