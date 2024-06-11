from rest_framework import serializers
from .models import Student,Classroom,Breakfast
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class ClassroomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"
class BreakfastModelSerializer(serializers.ModelSerializer):
      class Meta:
          model = Breakfast
          fields = "__all__"
