from django.urls import path
from . import views

#Create your urls here.
urlpatterns = [
    # path('students/', views.student_view, name="STUDENT MODEL"),
    path('professors/', views.professor_view, name="PROFESSOR MODEL"),
    path('subjects/', views.subject_view, name="SUBJECT MODEL"),
    path('programs/', views.program_view, name="PROGRAM MODEL"),
    path('enrollments/', views.enrollment_view, name="ENROLLMENT MODEL"),

    path('students/edit/<int:id>/', views.editStudentsInfo, name="REGISTER NEW USER"),
    path('students/', views.addNewStudents, name="STUDENT MODEL"),


    path('register/', views.RegisterUser, name='register'),
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('profile_view/', views.ProfileView, name='ProfileView')

]
