from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from work.serializers import serialset
from work.models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class helloworld(APIView):
    def get(self,request):
        return Response({'message':'hello world'}) 
    
class PostViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Post.objects.all()
    serializer_class=serialset
