from rest_framework import viewsets
from .serializers import FreelancerSerializer, EmployerSerializer
from .serializers import EmployeeSerializer, JobSerializer
from .models import Freelancer, Employer
from .models import Employee, Job

class FreelancerView(viewsets.ModelViewSet):
    serializer_class = FreelancerSerializer
    queryset = Freelancer.objects.all()

class EmployerView(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()

class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class JobView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
