from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def departments(request):
    message = """<div>
    <h1>LIST OF COURSES OFFERED</h1>
    <ul>
    <li>Bachelor of Science in Information Technology</li>
    <li>Bachelor of Arts in English Language Studies</li>
    <li>Bachelor of Science in Social Work</li>
    </ul>
    </div>"""

    return HttpResponse(message)


def enroll(request):
    message = '<h1>You have been enrolled to this Course.</h1>'

    return HttpResponse(message)

def unenroll(request):
    message = '<h1>You have been unenrolled to this Course.</h1>'

    return HttpResponse(message)