from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import FreelancerSerializer, EmployerSerializer
from .serializers import ProjectSerializer, EmployeeSerializer, JobSerializer
from .models import Freelancer, Employer
from .models import Project, Employee, Job

class FreelancerView(viewsets.ModelViewSet):
    serializer_class = FreelancerSerializer
    queryset = Freelancer.objects.all()

class EmployerView(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class JobView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
