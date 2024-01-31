from rest_framework import generics

from app.models import *
from app.serializers import CommentAPI


class CreateCommentAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentAPI

class UpdateCommentAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentAPI