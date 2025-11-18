from django.urls import path
from . import views

urlpatterns = [
    path('students/welcome/<str:name>', views.welcomeStudent, name="greet"),
    path('students/subjects', views.viewSubjects, name="subjects"),
    path('students/grades', views.studentGrades, name="grades"),
]
