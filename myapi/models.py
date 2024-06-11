from django.db import models

# Create your models here.
# i want to create onetoone field model for api 
# -> Person         -------   -> Address 
# a person has only one address . similarly
# a person has only one class room/level/faculty in a  college

# so   Student    -->   Classroom 

class  Student(models.Model):
    name = models.CharField(max_length=100)
    college_email = models.EmailField(unique=True)
    phone_number = models.IntegerField(max_length=100)
    address = models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    is_student = models.BooleanField(default=None)
    date_of_birth = models.DateTimeField()
    national_id = models.CharField(max_length=100,null=False)
    student_photo = models.ImageField(upload_to='emogi')
    def __str__(self):
        return f'{self.name}'

class Classroom(models.Model):
    time_from_home = models.TimeField(auto_now_add=True)
    distance_from_home = models.CharField(max_length=40)
    college_name = models.CharField(max_length=1000)
    section_name = models.CharField(max_length=10)
    student  = models.OneToOneField(Student,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.student}'

class Breakfast(models.Model):
  breakfast_type = models.CharField(max_length=100)
  breakfast_time = models.DateTimeField()
  breakfast_duration = models.CharField(max_length=50)
  breakfast_place = models.CharField(max_length=70)
  student_breakfast = models.OneToOneField(Student,on_delete=models.CASCADE,null= True)
