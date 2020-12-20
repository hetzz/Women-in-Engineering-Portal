from . import views
from django.urls import path, include
from django.conf.urls import url,include


urlpatterns =[
    path('studentProfile/', views.student_profile),
    path('login/',views.login),
    path('company_dashboard/<field>',views.company_dashboard),
    path('company_dashboard/',views.company_dashboard),
    path('signUp/',views.signUp),
    path('student_account/',views.student_account),
    path('logout/',views.logout),
    path('faculty_dashboard/',views.faculty_dashboard),
    path('faculty_student/',views.faculty_student),
    path('student_edit_profile/',views.student_edit_profile),
    path('faculty_dashboard/<student>',views.faculty_student_edit),
    path('',views.home)
]