from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Professor, Subject, Program, Enrollment
from .forms import StudentForm, RegisterForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def StudentView(req):
    student = Student.objects.all()

    if req.method == 'POST':
        form = StudentForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect('student')
    
    else:
        form = StudentForm()
        
    return render(req, 'student.html', {
        'form' : form,
        'students': student
        })

def editStudentsInfo(req, id):
    student = get_object_or_404(Student, id=id)
    print(student)
    if req.method == 'POST':
        form = StudentForm(req.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(req, 'success.html')
        
    else:
        form = StudentForm(instance=student)

    return render(req, 'edit_student.html', {'form' : form})
    


def RegisterUser(req):
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'User has been registered')
            return redirect('login')
        else:
            messages.error(req, 'User is not valid, please make sure to input a valid information.')
    else:
        form = RegisterForm()
    return render(req, 'register.html', {'form': form})

def LoginUser(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                messages.success(req, 'User Succesfully logged in.')
                return redirect('home')
            else:
                messages.error(req, 'User does not exist.')
        else:
            messages.error(req, 'Invalid user credentials')
    else:
        form = AuthenticationForm()

    return render(req, 'login.html', {'form':form})


def LogoutUser(req):
    logout(req)
    messages.info(req, 'User Successfully Logged Out.')
    return redirect('login')


def HomeView(req):
    return render(req, 'homepage.html')