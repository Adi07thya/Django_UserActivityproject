from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Member

class UserViewSet(viewsets.ModelViewSet):
    """
    API end points which does all the CRUD functionalities for Member Model
    """
    queryset = Member.objects.all()
    serializer_class = UserSerializer
