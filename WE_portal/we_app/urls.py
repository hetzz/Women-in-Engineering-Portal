from . import views
from django.urls import path, include
from django.conf.urls import url,include


urlpatterns =[
    path('studentProfile/', views.student_profile),
    path('login/',views.login),
    path('faculty_login/',views.faculty_login),
    path('company_login/',views.company_login),
    path('company_dashboard/',views.company_dashboard),
    path('signUp/',views.signUp),
    path('',views.home)
]