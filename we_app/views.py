from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import string
from pprint import pprint
from .models import Student, Student_profile, Faculty, Company,Faculty_Student,fields_of_interests,CsvFiles
from .forms import ResumeForm, CSVForm
from bs4 import BeautifulSoup
import csv as csv_pack
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
        try :
            student = Student.objects.filter(email_id=email)
            student = student[0]
            if student != None and student.password == password  :
                request.session['name'] = student.full_name
                return redirect(student_account)
            else:
                return render(request, 'login.html', context={'verify': 'Either Email or password is wrong :/'})
        except :
            pass
        try :
            faculty = Faculty.objects.filter(email_id=email)
            faculty = faculty[0]
            if faculty != None and faculty.password == password:
                request.session['name'] = faculty.faculty_name
                request.session['email'] = faculty.email_id
                return redirect(faculty_dashboard)
            else:
                return render(request, 'login.html', context={'verify': 'Either Email or password is wrong :/'})
        except :
            pass
        try :
            company = Company.objects.filter(email_id=email)
            company = company[0]
            if company != None and company.password == password:
                request.session['name'] = company.company_name
                return redirect(company_dashboard)
            else:
                return render(request, 'login.html', context={'verify': 'Either Email or password is wrong :/'})
        except :
            pass

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
            resume = ResumeForm(request.POST, request.FILES)
            if resume.is_valid():
                profile.resume = request.FILES['resume']
            else:
                form = ResumeForm()
            f = profile.first_interest = request.POST.get('first_interest')
            s = profile.second_interest = request.POST.get('second_interest')
            t = profile.third_interest = request.POST.get('third_interest')
            ft = profile.fourth_interest = request.POST.get('fourth_interest')
            profile.github_link = request.POST.get('github_link')
            profile.gitlab_link = request.POST.get('gitlab_link')
            profile.linkdIn_link = request.POST.get('linkdIn_link')
            profile.Other = request.POST.get('Other')
            profile.save()
            check_fields = [f,s,t,ft]
            fields_objects = getStudentsInterests()
            for field in check_fields :
                if field not in fields_objects :
                    new_field = fields_of_interests()
                    new_field.fields = field
                    new_field.save()
            profile = Student_profile.objects.filter(full_name = student)
            profile = profile[0]
            return redirect(student_account)

def student_edit_profile(request):
    context = {'username' : request.session['name'], 'students' :[]}
    if request.method == 'GET':
        try :
            student = Student_profile.objects.filter(full_name = request.session['name'])
            student = student[0]
            STUDENT = {}
            STUDENT = student.__dict__
            context['students'].append(STUDENT)
        except :
            pass
        return render(request,'student_edit_profile.html',context)
    else :
        profile = Student_profile.objects.filter(full_name = request.session['name'])
        profile = profile[0]
        profile.full_name = request.POST.get('FullName')
        profile.email_id = request.POST.get('email')
        profile.about = request.POST.get('About')
        profile.qualification = request.POST.get('Degree')
        profile.tag_line = request.POST.get('Tag Line')
        resume = ResumeForm(request.POST, request.FILES)
        if resume.is_valid():
            profile.resume = request.FILES['resume']
        else:
            form = ResumeForm()
        f = profile.first_interest = request.POST.get('first_interest')
        s = profile.second_interest = request.POST.get('second_interest')
        t = profile.third_interest = request.POST.get('third_interest')
        ft = profile.fourth_interest = request.POST.get('fourth_interest')
        profile.github_link = request.POST.get('github_link')
        profile.gitlab_link = request.POST.get('gitlab_link')
        profile.linkdIn_link = request.POST.get('linkdIn_link')
        profile.Other = request.POST.get('Other')
        print(profile.__dict__)
        profile.save()
        check_fields = [f,s,t,ft]
        fields_objects = getStudentsInterests()
        for field in check_fields :
            if field not in fields_objects :
                new_field = fields_of_interests()
                new_field.fields = field
                new_field.save() 
        return redirect(student_account)

def student_account(request):
    context = {'username' : request.session['name'], 'student' : {} }
    STUDENTS = fetchStudents(request,None)
    for student in STUDENTS :
        if(student['full_name'] == request.session['name']) :
            context['student'] = student
    return render(request,"student_account.html",context)

def company_dashboard(request, field = None):
    context = {'username' : request.session['name'], 'student' : [],'fields' :[]}
    FIELDS = getStudentsInterests()
    context['fields'] = []
    for f in FIELDS :
        context['fields'].append(f)
    if request.method == 'GET' and field == None:
        if request.session['name'] == "" :
            return redirect(login)
        else :
            context['username'] = request.session['name']
            STUDENTS = fetchStudents(request,'all')
            context['students'] = []
            for student in STUDENTS :
                context['students'].append(student)
            return render(request, 'company_dashboard.html',context)
    
    else :
        STUDENTS = fetchStudents(request,field)
        context['students'] = []
        for student in STUDENTS :
            context['students'].append(student)
        return render(request, 'company_dashboard.html',context)
        
def fetchStudents(request , field) :
    STUDENTS = []
    students = Student_profile.objects.all()
    for student in students :
        STUDENT = {}
        STUDENT = student.__dict__
        try :
            fs = Faculty_Student.objects.filter(student_name = STUDENT['full_name'])
            FACULTY_STUDENT = fs[0].__dict__
            STUDENT.update(FACULTY_STUDENT)
        except :
            pass
        STUDENTS.append(STUDENT)
    if field == 'all' or field == None:
        return STUDENTS
    else :
        rem = []
        for STUDENT in STUDENTS :
            if  field not in STUDENT.values():
                rem.append(STUDENT)
        for i in rem :
            STUDENTS.remove(i)
        #STUDENTS = sorted(STUDENTS, key=lambda x: x['faculty_points'], reverse=True)
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
            try :
                csv = CsvFiles.objects.filter(faculty_email_id = request.session['email'])
                context['csv'] = csv[0].csv
            except :
                pass
            return render(request, 'faculty_dashboard.html',context)
    else :
        CSV = CSVForm(request.POST, request.FILES)
        # if csv.is_valid():
        try:
            faculty_csv = CsvFiles.objects.filter(faculty_email_id = request.session['email'])
            faculty_csv = faculty_csv[0]
            faculty_csv.csv = request.FILES['csv']
            faculty_csv.save()
        except:
            faculty_csv = CsvFiles()
            faculty_csv.faculty_email_id = request.session['email']
            faculty_csv.csv = request.FILES['csv']
            faculty_csv.save()
        with open('/home/hetal/Projects/Women-in-Engineering-Portal/WE_portal/media/CSV/'+str(request.FILES['csv']),'rt')as f:
            data = csv_pack.reader(f)
            for row in data:
                try :
                    fs = Faculty_Student.objects.filter(student_name = row[0])
                    fs = fs[0]
                    print('Yes')
                except :
                    print("no")
                    fs = Faculty_Student()
                fs.faculty_name = request.session['name']
                fs.faculty_email_id = request.session['email']
                fs.student_name = row[0]
                fs.student_email_id = row[1]
                fs.faculty_grade = row[3]
                fs.faculty_points = row[4]
                fs.faculty_review = row[2]
                fs.save()
        # else:
        #     print("Invalid")
        #     form = CSVForm()    
        #print(request.FILES['csv'])
        
        return redirect(faculty_dashboard)

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
        fs.student_name = request.POST.get('full_name')
        fs.student_email_id = request.POST.get('email')
        fs.faculty_grade = request.POST.get('faculty_grade')
        fs.faculty_points = request.POST.get('faculty_points')
        fs.faculty_review = request.POST.get('faculty_review')
        fs.save()
        return redirect(faculty_dashboard)

def faculty_student_edit(request , student = None):
    context = {'username' :request.session['name'], 'facstu' : []}
    if request.method == 'GET' and student != None:
        fs = Faculty_Student.objects.filter(faculty_name = request.session['name']).filter(student_name = student)
        fs = fs[0]
        FS = {}
        FS = fs.__dict__
        context['facstu'].append(FS)
        return render(request,'faculty_student_edit.html',context)
    else :
        fs = Faculty_Student.objects.filter(faculty_name = request.session['name'])
        fs = fs[0]
        fs.faculty_name = request.session['name']
        fs.faculty_email_id = request.session['email']
        fs.student_name = request.POST.get('full_name')
        fs.student_email_id = request.POST.get('email')
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
            FS = fs.__dict__
            FACSTU.append(FS)
        FACSTU = sorted(FACSTU, key=lambda x: x['faculty_points'], reverse=True)
        return FACSTU   
    except :
        pass        

def getStudentsInterests():
    fields = fields_of_interests.objects.all()
    field = []
    for f in fields :
        field.append(f.fields)
    return field

def home(request):
    return render(request, "home.html")
