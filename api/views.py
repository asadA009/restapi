from django.shortcuts import render
#from rest_framework import serializers
from .models import student
from django.http import HttpResponse
from .serializers import studentSerializers
from rest_framework.renderers import JSONRenderer
def student_detail(request):
    stu=student.objects.all()
    serializer=studentSerializers(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

    
