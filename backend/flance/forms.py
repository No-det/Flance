from django.forms import ModelForm
from .models import Freelancer

class SignUpForm(ModelForm):
    class Meta:
        model = Freelancer
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

class FreelancerProfileForm(ModelForm):
    class Meta:
        model = Freelancer
        fields = ['languages', 'feld', 'specialization', 'level']
