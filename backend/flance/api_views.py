from rest_framework import viewsets
from .serializers import FreelancerSerializer, EmployerSerializer
from .serializers import EmployeeSerializer, JobSerializer
from .models import Freelancer, Employer
from .models import Employee, Job

class FreelancerView(viewsets.ModelViewSet):
    serializer_class = FreelancerSerializer
    queryset = Freelancer.objects.all()
    # Example for api route
    def get_user(request) :
    if request.method == 'GET' :
        data = {
            'data': 'THIS IS THE PROTECTED STRING FROM SERVER', #this is where the data to be sent goes, this has to be taken from db
        }

        return Response(data, status=status.HTTP_200_OK) #this is how you send data to front end as json I hope

class EmployerView(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()

class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class JobView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
