from rest_framework import serializers
from .models import Freelancer, Employer, User
from .models import Employee, Job

class FreelancerSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        freelancer = User(
            first_name=self.validated_data['first_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        freelancer.set_password(password)
        freelancer.is_freelancer = True
        freelancer.save()
        return freelancer


class EmployerSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        employer = User(
            first_name=self.validated_data['first_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        employer.set_password(password)
        employer.is_employer = True
        employer.save()
        return employer

class FreelancerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancer
        fields = ('languages', 'fields', 'specialization', 'level', 'salary')

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('user', 'name', 'comapany', 'website')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employer', 'time_for_completion')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job', 'languages', 'fields', 'specialization', 'level', 'salary')
