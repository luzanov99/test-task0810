from django.shortcuts import render
from  django.http import HttpResponse
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .models import DataUser
from .serializers import UserSerialiser

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset=DataUser.objects.all()
    serializer_class=UserSerialiser


def add_user(request):
    user=DataUser(username="user1", email="admin@gmail.com")
    user.save()
    return HttpResponse("OKs")


