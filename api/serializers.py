from rest_framework import serializers
from .models import student

class confrenceserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=('name','roll','city')