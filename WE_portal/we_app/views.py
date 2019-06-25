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
            
        elif request.POST.get('Faculty', None):
            faculty = Faculty()
            faculty.Faculty_id = ID
            faculty.full_name = full_name
            faculty.email_id = email
            faculty.password = password
            faculty.save()

        elif request.POST.get('Company', None):
            company = Company()
            company.Company_id = ID
            company.full_name = full_name
            company.email_id = email
            company.password = password
            company.save()
            
    return redirect(login)


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if request.POST.get('Student', None):
            student = Student.objects.filter(email_id=email)
            student = student[0]
            if student.password == password:
                request.session['name'] = student.full_name
                return redirect(student_profile)
            else:
                return render(request, 'login.html', context={'verify': 'Wrong Password :/'})
        elif request.POST.get('Faculty', None):
            faculty = Faculty.objects.filter(email_id=email)
            faculty = faculty[0]
            if faculty.password == password:
                request.session['name'] = faculty.full_name
                return redirect(student_profile)
            else:
                return render(request, 'login.html', context={'verify': 'Wrong Password :/'})
        
        elif request.POST.get('Company', None):
            company = Company.objects.filter(email_id=email)
            company = company[0]
            if company.password == password:
                request.session['name'] = company.full_name
                return redirect(company_dashboard)
            else:
                return render(request, 'login.html', context={'verify': 'Wrong Password :/'})
       



def student_profile(request):
    if request.method == 'GET':
        return render(request, 'student_profile.html')

def company_dashboard(request):
    return render(request, "company_dashboard.html")


def home(request):
    return render(request, "home.html")
