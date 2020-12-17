from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from apka import models
from . import serializers
from .models import Post


from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

class HelloView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  
            'auth': str(request.auth),  
        }
        return Response(content)
        
class PostViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

