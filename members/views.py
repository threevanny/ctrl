from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer