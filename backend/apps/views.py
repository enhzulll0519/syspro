from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializers
# Create your views here.
class TodoGetCreate(generics.ListCreateAPIView):
    queryset=Todo.objects.all() 
    serializer_class=TodoSerializers # Харах бүртгэх үйлдэл хийх боломжтой класс


class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers
