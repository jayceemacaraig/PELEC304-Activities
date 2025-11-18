from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def welcomeStudent(request, name):
    message = f"<h1>Hello, Welcome Student {name}</h1>"
    return HttpResponse(message)

def viewSubjects(request):
    message = """<div>
    <h1>LIST OF SUBJECTS</h1>
    <ul>
    <li>ITCS01</li>
    <li>ITCS02</li>
    <li>ITCS03</li>
    </ul>
    </div>"""

    return HttpResponse(message)


def studentGrades(request):
    message = """
    <div>
    <h1>GRADES</h1>
    <ul>
    <li>ITCS01 : 97</li>
    <li>ITCS02 : 99</li>
    <li>ITCS03 : 87</li>
    </ul>
    </div>"""

    return HttpResponse(message)

