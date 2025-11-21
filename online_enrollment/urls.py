from django.urls import path
from . import views

#Create your urls here.
urlpatterns = [
    path('register/', views.RegisterUser, name='register'),
    path('', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('home/', views.HomeView, name='home'),
    path('student/', views.StudentView, name='student')
]
