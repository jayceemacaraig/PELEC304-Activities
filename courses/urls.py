from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.departments, name='courses_offered'),
    path('courses/enroll', views.enroll, name='enroll'),
    path('courses/unenroll', views.unenroll, name='unenroll'),
]