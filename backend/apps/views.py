from django.shortcuts import render
from rest_framework import generics
from .models import Todo, List
from .serializers import TodoSerializers, ListSerializers
# Create your views here.
class TodoGetCreate(generics.ListCreateAPIView):
    queryset=Todo.objects.all() 
    serializer_class=TodoSerializers # Харах бүртгэх үйлдэл хийх боломжтой класс
class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers


class ListGetCreate(generics.ListCreateAPIView):
    queryset=List.objects.all() 
    serializer_class=ListSerializers # Харах бүртгэх үйлдэл хийх боломжтой класс
class ListUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=List.objects.all()
    serializer_class=ListSerializers
