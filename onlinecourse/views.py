from django.shortcuts import render
from django.http import HttpResponse


def submit(request, course_id):
    return HttpResponse("Exam submitted")


def show_exam_result(request, course_id, submission_id):
    return HttpResponse("Exam result")
