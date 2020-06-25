from rest_framework import serializers
from .models import Freelancer, Employer
from .models import Employee, Job

class FreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancer
        fields = ('id', 'first_name', 'username', 'email', 'languages', 'fields', 'specialization', 'level', 'salary')

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('comapany', 'website')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employer', 'time_for_completion')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job', 'languages', 'fields', 'specialization', 'level', 'salary')
