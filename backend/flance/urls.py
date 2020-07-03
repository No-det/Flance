from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/freelancer/', views.freelancer_reg, 'reg_freelancer'),
    path('register/employer/', views.employer_reg, 'reg_employer'),
    path('create/freelancer/', views.FreelancerProfileSerializer, 'create_freelancer_profile'),
    path('create/employer/', views.EmployerProfileSerializer, 'create_employer_profile')
]