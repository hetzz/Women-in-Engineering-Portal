from . import views
from django.urls import path, include
from django.conf.urls import url,include

urlpatterns =[
    path('student/', views.student)
]