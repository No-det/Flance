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



'''
class Languages(models.TextChoices):
        VISUAL_BASIC_NET = 'Visual Basic .NET'
        OBJECTIVE_C = 'Objective-C'
        JAVASCRIPT = 'JavaScript'
        PYTHON = 'Python'
        C_HASH = 'C#'
        SWIFT = 'Swift'
        JAVA = 'Java'
        RUBY = 'Ruby'
        PERL = 'Perl'
        CPP = 'C++'
        PHP = 'PHP'
        SQL = 'SQL'
        GO = 'Go'
        C = 'C'
        R = 'R'

    class Fields(models.TextChoices):
        DESKTOP_APP = 'Desktop App Developer'
        ANDROID_APP = 'Android App Developer'
        IOS_APP = 'iOS App Developer'
        WEB_APP = 'Web App Developer'
        ML = 'Machine Learning'
        AI = 'Artificial Intelligence'

    class Specialization(models.TextChoices):
        FED = 'Front End Developer'
        BED = 'Back End Developer'
        FSD = 'Full Stack Developer'
    
    class Level(models.TextChoices):
        BEG = 'Beginner'
        EXP = 'Experienced'
        PRO = 'Pro'
'''