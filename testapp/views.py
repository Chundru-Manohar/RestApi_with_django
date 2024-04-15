from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
# Create your views here.
@api_view(['GET'])
def home(request):
    stud_obj = Student.objects.all()
    serial = StudentSerializer(stud_obj,many=True)
    return Response(serial.data)

@api_view(['POST'])
def Student_adds(request):
    stud_obj = Student.objects.all()
    serial = StudentSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)
    
@api_view(['POST'])
def Student_update(request,id):
    stud_obj = Student.objects.get(id=id)
    serial = StudentSerializer(instance=stud_obj,data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)
      
    
@api_view(['DELETE'])
def Student_delete(request,id):
    stud_obj = Student.objects.get(id=id)
    stud_obj.delete()
    return Response("DATA has been deleted")
      
    