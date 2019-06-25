from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import string
from pprint import pprint
from .models import Student, Student_profile, Faculty, Company
# Create your views here.


def signUp(request):
    if request.method == 'GET':
        return render(request, 'signUp.html')
    else:
        ID = request.POST.get('ID', None)
        full_name = request.POST.get('Full_name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if request.POST.get('Student', None):
            student = Student()
            student.student_id = ID
            student.full_name = full_name
            student.email_id = email
            student.password = password
            student.save()
            print('Yes')
            return redirect(student_login)
        elif request.POST.get('Faculty', None):
            faculty = Faculty()
            faculty.Faculty_id = ID
            faculty.full_name = full_name
            faculty.email_id = email
            faculty.password = password
            faculty.save()
            return render(request, 'faculty_login.html')
        elif request.POST.get('Company', None):
            company = Company()
            company.Company_id = ID
            company.full_name = full_name
            company.email_id = email
            company.password = password
            company.save()
            return render(request, 'company_login.html')
    return render(request, 'signUp.html')


def student_profile(request):
    if request.method == 'GET':
        return render(request, 'student_profile.html')


def student_login(request):
    if request.method == 'GET':
        return render(request, "student_login.html")
    else:
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        student = Student.objects.filter(email_id=email)
        student = student[0]
    if student.password == password:
        request.session['name'] = student.full_name
        return redirect(student_profile)
    else:
        return render(request, 'student_login.html', context={'verify': 'Wrong Password :/'})


def faculty_login(request):
    return render(request, "faculty_login.html")


def company_login(request):
    return render(request, "company_login.html")


def company_dashboard(request):
    return render(request, "company_dashboard.html")


def home(request):
    return render(request, "home.html")
