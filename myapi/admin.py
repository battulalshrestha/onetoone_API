from django.contrib import admin
from .models import Student,Classroom,Breakfast
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ['id','college_email','phone_number','address','password','is_student','date_of_birth','national_id','student_photo']

@admin.register(Classroom)
class Classroomadmin(admin.ModelAdmin):
    list_display = ['id','time_from_home','distance_from_home','college_name','section_name','student']
    
@admin.register(Breakfast)
class Breakfastadmin(admin.ModelAdmin):
    list_display = ['id','breakfast_type','breakfast_time','breakfast_duration','breakfast_place','student_breakfast']

