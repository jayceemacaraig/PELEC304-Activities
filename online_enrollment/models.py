from django.db import models

# Create your models here.
class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_level = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField()
    student_ID = models.CharField(max_length=5)
    program_title = models.CharField(max_length=100)

    def __str__(self):
        return f'Student : {self.first_name} {self.last_name}'

class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    honorofics = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField()
    employee_ID = models.CharField(max_length=5)
    program_title = models.CharField(max_length=100)

    def __str__(self):
        return f'Professor : {self.first_name} {self.last_name}'
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    units = models.IntegerField()
    status = models.CharField(max_length=50)
    employee_ID = models.CharField(max_length=5)
    subject_ID = models.CharField(max_length=10)

    def __str__(self):
        return f'Subject : {self.subject_name}'
    
class Program(models.Model):
    program_title = models.CharField(max_length=100)
    program_head = models.CharField(max_length=100)
    degree_duration = models.IntegerField()
    number_of_students = models.IntegerField()
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return f'Program : {self.program_title}'
    
class Enrollment(models.Model):
    enrollment_status = models.CharField(max_length=10)
    student_ID = models.CharField(max_length=5)
    program_title = models.CharField(max_length=100)
    balance = models.FloatField()
    program_head = models.CharField(max_length=100)

    def __str__(self):
        return f'Enrollment status of student : {self.student_ID}'
