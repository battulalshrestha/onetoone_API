# class based api views
from django.shortcuts import render
from rest_framework import generics
from .models import Student,Classroom,Breakfast
from .serializers import StudentModelSerializer,ClassroomModelSerializer,BreakfastModelSerializer
class Studentlistcreate(generics.ListCreateAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentModelSerializer

class Classroomlistcreate(generics.ListCreateAPIView):
   queryset = Classroom.objects.all()
   serializer_class = ClassroomModelSerializer
   
class  Breakfastlistcreate(generics.ListCreateAPIView):
   queryset = Breakfast.objects.all()
   serializer_class = BreakfastModelSerializer