from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def signup(request):
    message = """<h1>SIGNUP</h1>
    <h3>USERNAME</h3>
    <input type='name'>
    <h3>PASSWORD</h3>
    <input type='password'>"""

    return HttpResponse(message)


def delete(request):
    message = "<h1>Account has been deleted.</h1>"

    return HttpResponse(message)


def changePassword(request):
    message = """<h1>CHANGE PASSWORD</h1>
    <h3>PUT NEW PASSWORD:</h3>
    <input type='password'>
    <h3>PUT NEW PASSWORD AGAIN TO CONFIRM:</h3>
    <input type='password'>"""
   
    return HttpResponse(message)