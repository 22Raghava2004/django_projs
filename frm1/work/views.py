from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from work.serializers import serialset
from work.models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from work.permissions import IsPostPossessor
from rest_framework import filters
from work.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class helloworld(APIView):
    def get(self,request):
        return Response({'message':'hello world'}) 
    
class PostViewSet(ModelViewSet):

    permission_classes=[IsAuthenticated,IsPostPossessor]
    filter_backends=[filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    ordering_fields=['id']
    search_fields=['title','content']
    filterset_class=PostFilter
    # queryset=Post.objects.all()  # this is to fetch all objects from Post model
    serializer_class=serialset

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)
