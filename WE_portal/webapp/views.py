from django.shortcuts import render, redirect
from datetime import datetime
from django.http import JsonResponse, HttpResponse
import random
import string
from pprint import pprint
# Create your views here.


def student(request):
    if request.method == 'GET':
        return render(request, 'student.html')
