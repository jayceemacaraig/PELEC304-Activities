from django.contrib import admin
from .models import TestingDatabase, Student, Professor, Subject, Program, Enrollment


# Register your models here.
admin.site.register(TestingDatabase)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(Program)
admin.site.register(Enrollment)