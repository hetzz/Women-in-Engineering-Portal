from django.db import models

# Create your models here.
class Student(models.Model) :
    student_id = models.CharField(max_length = 50)
    full_name = models.CharField(max_length = 150, default = 'Student')
    email_id = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class Student_profile(models.Model):
    full_name = models.CharField(max_length = 100,default = 'Student')
    email_id = models.CharField(max_length = 100,default = 'NA')
    about = models.CharField(max_length = 500)
    qualification = models.CharField(max_length = 50)
    tag_line = models.CharField(max_length = 200, default = qualification)
    resume = models.FileField(null = True, blank = True)
    first_interest = models.CharField(max_length = 50 , default = None)
    second_interest = models.CharField(max_length = 50, default = None)
    third_interest = models.CharField(max_length = 50, default = None)
    fourth_interest = models.CharField(max_length = 50, default = None)
    github_link = models.CharField(max_length = 100,default = None)
    gitlab_link = models.CharField(max_length = 100, default = None)
    linkdIn_link = models.CharField(max_length = 100, default = None)
    Other = models.CharField(max_length = 100, default = None)
    faculty_review = models.CharField(max_length = 1000, default = 'Good')
    faculty_points = models.IntegerField(default = 50)
    faculty_grade = models.CharField(max_length = 10, default = 'C')

class Faculty(models.Model):
    Faculty_id = models.CharField(max_length = 50)
    faculty_name = models.CharField(max_length = 150, default = 'Faculty')
    email_id = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)



class Company(models.Model):
    Company_id = models.CharField(max_length = 50)
    company_name = models.CharField(max_length = 150, default = 'Company')
    email_id = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class Company_Student(models.Model):
    Company_name = models.CharField(max_length = 150, default = "Company")
    invited_students = models.CharField(max_length = 100 , default = "")