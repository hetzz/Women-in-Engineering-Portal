from . import views
from django.urls import path, include
from django.conf.urls import url,include


urlpatterns =[
    path('studentProfile/', views.student_profile),
    path('login/',views.login),
    path('company_dashboard/',views.company_dashboard),
    path('signUp/',views.signUp),
    path('student_account/',views.student_account),
    path('logout/',views.logout),
    path('',views.home)
]