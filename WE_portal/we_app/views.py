from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import string
from pprint import pprint
from .models import Student, Student_profile, Faculty, Company,Faculty_Student
from bs4 import BeautifulSoup
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
            request.session['name'] = full_name
            request.session['email'] = email
            return redirect(student_profile)
            
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
        
        else :
            context = {'verify' : "Please Select a radio Button"}
            return render(request,"signUp.html",context)
            
    return redirect(login)


def login(request):
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
                return redirect(student_account)
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
                request.session['email'] = faculty.email_id
                return redirect(faculty_dashboard)
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
        if student == request.POST.get('FullName'):
            profile = Student_profile()
            profile.full_name = request.POST.get('FullName')
            profile.email_id = request.POST.get('email')
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
            return redirect(student_account)

def student_edit_profile(request):
    context = {'username' : request.session['name'], 'students' :[]}
    if request.method == 'GET':
        student = Student_profile.objects.filter(full_name = request.session['name'])
        student = student[0]
        STUDENT = {}
        STUDENT['full_name'] = request.session['name']
        STUDENT['email'] = student.email_id
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
        context['students'].append(STUDENT)
        return render(request,'student_edit_profile.html',context)
    else :
        profile = Student_profile.objects.filter(full_name = request.session['name'])
        profile = profile[0]
        profile.full_name = request.POST.get('FullName')
        profile.email_id = request.POST.get('email')
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
        return redirect(student_account)



def student_account(request):
    context = {'username' : request.session['name'], 'student' : {} }
    STUDENTS = fetchStudents(request)
    for student in STUDENTS :
        if(student['full_name'] == request.session['name']) :
            context['student'] = student
    return render(request,"student_account.html",context)

def company_dashboard(request):
    context = {'username' : request.session['name'], 'student' : []}
    if request.method == 'GET':
        if request.session['name'] == "" :
            return redirect(login)
        else :
            context['username'] = request.session['name']
            STUDENTS = fetchStudents(request)
            context['students'] = []
            for student in STUDENTS :
                context['students'].append(student)
            return render(request, 'company_dashboard.html',context)

def fetchStudents(request) :
    STUDENTS = []
    students = Student_profile.objects.all()
    for student in students :
        STUDENT = {}
        STUDENT['full_name'] = student.full_name
        STUDENT['email'] = student.email_id
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
        try :
            stu_faculty = Faculty_Student.objects.filter(full_name = student.full_name)
            stu_faculty = stu_faculty[0]
            STUDENT['faculty_review'] = stu_faculty.faculty_review
            STUDENT['faculty_points'] = stu_faculty.faculty_points
            STUDENT['faculty_grade'] = stu_faculty.faculty_grade
        except :
            pass
        STUDENTS.append(STUDENT)
    # STUDENTS = sorted(STUDENTS, key=lambda x: x['faculty_points'], reverse=True)
    return STUDENTS

def faculty_dashboard(request):
    context = {'username' : request.session['name'], 'facstu' : []}
    if request.method == 'GET':
        if request.session['name'] == "" :
            return redirect(login)
        else :
            FACSTU = fetchFacultyStudent(request)
            for fs in FACSTU :
                context['facstu'].append(fs)
            return render(request, 'faculty_dashboard.html',context)

def faculty_student(request):
    context = {'username' : request.session['name']}
    if request.method == 'GET':
        if request.session['name'] == "" :
            return redirect(login)
        else :
            return render(request,"faculty_student.html",context)
    else :
        fs = Faculty_Student()
        fs.faculty_name = request.session['name']
        fs.faculty_email_id = request.session['email']
        fs.full_name = request.POST.get('full_name')
        fs.email_id = request.POST.get('email')
        fs.faculty_grade = request.POST.get('faculty_grade')
        fs.faculty_points = request.POST.get('faculty_points')
        fs.faculty_review = request.POST.get('faculty_review')
        fs.save()
        return redirect(faculty_dashboard)

def faculty_student_edit(request):
    context = {'username' :request.session['name'], 'facstu' : []}
    if request.method == 'GET' :
        soup = BeautifulSoup('/home/hetal/Projects/we_portal/WE_portal/we_app/templates/faculty_dashboard.html')
        name_tag = soup.find('h4', itemprop='name')
        print(name_tag)
        fs = Faculty_Student.objects.filter(faculty_name = request.session['name'])
        fs = fs[0]
        FS = {}
        FS['student_name'] = fs.full_name
        FS['email'] = fs.email_id
        FS['faculty_grade'] = fs.faculty_grade
        FS['faculty_points'] = fs.faculty_points
        FS['faculty_review'] = fs.faculty_review
        context['facstu'].append(FS)
        return render(request,'faculty_student_edit.html',context)
    else :
        fs = Faculty_Student.objects.filter(faculty_name = request.session['name'])
        fs = fs[0]
        fs.faculty_name = request.session['name']
        fs.faculty_email_id = request.session['email']
        fs.full_name = request.POST.get('full_name')
        fs.email_id = request.POST.get('email')
        fs.faculty_grade = request.POST.get('faculty_grade')
        fs.faculty_points = request.POST.get('faculty_points')
        fs.faculty_review = request.POST.get('faculty_review')
        fs.save()
        return redirect(faculty_dashboard)

def fetchFacultyStudent(request):
    FACSTU = []
    try :
        facstu = Faculty_Student.objects.filter(faculty_name = request.session['name'])
        for fs in facstu :
            FS = {}
            FS['student_name'] = fs.full_name
            FS['email'] = fs.email_id
            FS['faculty_grade'] = fs.faculty_grade
            FS['faculty_points'] = fs.faculty_points
            FS['faculty_review'] = fs.faculty_review
            FACSTU.append(FS)
        FACSTU = sorted(FACSTU, key=lambda x: x['faculty_points'], reverse=True)
        return FACSTU   
    except :
        pass        
    

def home(request):
    return render(request, "home.html")

