from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/freelancer/', views.freelancer_reg, name='reg_freelancer'),
    path('register/employer/', views.employer_reg, name='reg_employer'),
    path('create/freelancer/', views.FreelancerProfileSerializer, name='create_freelancer_profile'),
    path('create/employer/', views.EmployerProfileSerializer, name='create_employer_profile')
]