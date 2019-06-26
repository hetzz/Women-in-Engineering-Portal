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
            faculty.faculty_name = full_name
            faculty.email_id = email
            faculty.password = password
            faculty.save()

        elif request.POST.get('Company', None):
            company = Company()
            company.Company_id = ID
            company.company_name = full_name
            company.email_id = email
            company.password = password
            company.save()
            
    return redirect(login)


def login(request):
    # try:
    #     if request.session['name']:
    #         context = {'username':request.session['name'], 'login_status':0}
    #     else:
    #         context = {'username':'public','login_status':1}
    # except:
    #     pass
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if request.POST.get('Student', None):
            try :
                student = Student.objects.filter(email_id=email)
                student = student[0]
            except :
                student = None
            if student != None and student.password == password  :
                request.session['name'] = student.full_name
                return redirect(student_profile)
            else:
                return render(request, 'login.html', context={'verify': 'Either Email or password is wrong :/'})
        elif request.POST.get('Faculty', None):
            try :
                faculty = Faculty.objects.filter(email_id=email)
                faculty = faculty[0]
            except :
                faculty = None
            if faculty != None and faculty.password == password:
                request.session['name'] = faculty.faculty_name
                return redirect(student_profile)
            else:
                return render(request, 'login.html', context={'verify': 'Either Email or password is wrong :/'})
        
        elif request.POST.get('Company', None):
            try :
                company = Company.objects.filter(email_id=email)
                company = company[0]
            except :
                company = None
            if company != None and company.password == password:
                request.session['name'] = company.company_name
                return redirect(company_dashboard)
            else:
                return render(request, 'login.html', context={'verify': 'Either Email or password is wrong :/'})
       
def logout(request):
    if request.method=='GET':
        request.session['name'] = ''
        return redirect(home)

def student_profile(request):
    context = {'username' : request.session['name']}
    if request.method == 'GET':
        if request.session['name'] == "" :
            return redirect(login)
        else :
            return render(request, 'student_profile.html',context)
    else :
        student = request.session['name']
        print(student)
        print(request.POST.get('FullName'))
        if student == request.POST.get('FullName'):
            print("Yes")
            profile = Student_profile()
            profile.full_name = request.POST.get('FullName')
            profile.email_id = Student.email_id
            profile.about = request.POST.get('About')
            profile.qualification = request.POST.get('Degree')
            profile.tag_line = request.POST.get('Tag Line')
            #profile.resume = request.POST.get('Resume')
            profile.first_interest = request.POST.get('first_interest')
            profile.second_interest = request.POST.get('second_interest')
            profile.third_interest = request.POST.get('third_interest')
            profile.fourth_interest = request.POST.get('fourth_interest')
            profile.github_link = request.POST.get('github_link')
            profile.gitlab_link = request.POST.get('gitlab_link')
            profile.linkdIn_link = request.POST.get('linkdIn_link')
            profile.Other = request.POST.get('Other')
            profile.save()
            profile = Student_profile.objects.filter(full_name = student)
            profile = profile[0]
            print(profile)
            return redirect(student_account)

def student_account(request):
    return render(request,"student_account.html")

def company_dashboard(request):
    context = {'username' : request.session['name'], 'student' : []}
    if request.method == 'GET':
        if request.session['name'] == "" :
            return redirect(login)
        else :
            context['username'] = request.session['name']
            STUDENTS = fetchStudents()
            context['students'] = []
            for student in STUDENTS :
                context['students'].append(student)
            return render(request, 'company_dashboard.html',context)

def fetchStudents() :
    STUDENTS = []
    students = Student_profile.objects.all()
    for student in students :
        STUDENT = {}
        STUDENT['full_name'] = student.full_name
        # STUDENT[]
        STUDENT['about'] = student.about
        STUDENT['qualification'] = student.qualification
        STUDENT['tag_line'] = student.tag_line
        STUDENT['resume'] = student.resume
        STUDENT['first_interest'] = student.first_interest
        STUDENT['second_interest'] = student.second_interest
        STUDENT['third_interest'] = student.third_interest
        STUDENT['fourth_interest'] = student.fourth_interest
        STUDENT['github_link'] = student.github_link
        STUDENT['gitlab_link'] = student.gitlab_link
        STUDENT['linkdIn_link'] = student.linkdIn_link
        STUDENT['other'] = student.Other
        STUDENT['faculty_review'] = student.faculty_review
        STUDENT['faculty_points'] = student.faculty_points
        STUDENTS.append(STUDENT)
    STUDENTS = sorted(STUDENTS, key=lambda x: x['faculty_points'], reverse=True)
    return STUDENTS

def home(request):
    return render(request, "home.html")

