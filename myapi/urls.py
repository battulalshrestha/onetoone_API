from django.urls import path
from .views import Studentlistcreate, Classroomlistcreate,Breakfastlistcreate
urlpatterns = [
  #  path('onetoone/',)
  path('student/',Studentlistcreate.as_view()),
  path('classroom/',Classroomlistcreate.as_view()),
  path('breakfast/',Breakfastlistcreate.as_view())

]
