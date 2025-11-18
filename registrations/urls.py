from django.urls import path
from . import views

urlpatterns = [
    path('registration/signup', views.signup, name='signup'),
    path('registration/delete', views.delete, name='delete'),
    path('registration/change-password', views.changePassword, name='changePassword'),
]