from rest_framework import serializers
from .models import Todo, List

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields='__all__'

class ListSerializers(serializers.ModelSerializer):
    class Meta:
        model=List
        fields='__all__'