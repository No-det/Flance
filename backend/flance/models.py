from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator as max_value
from django.core.validators import MinValueValidator as min_value

LANGUAGES = [
        ('VISUAL_BASIC_NET', 'Visual Basic .NET'),
        ('OBJECTIVE_C', 'Objective-C'),
        ('JAVASCRIPT', 'JavaScript'),
        ('PYTHON', 'Python'),
        ('C_HASH', 'C#'),
        ('SWIFT', 'Swift'),
        ('JAVA', 'Java'),
        ('RUBY', 'Ruby'),
        ('PERL', 'Perl'),
        ('CPP', 'C++'),
        ('PHP', 'PHP'),
        ('SQL', 'SQL'),
        ('GO', 'Go'),
        ('C', 'C'),
        ('R', 'R')
]

FIELDS = [
        ('DESKTOP_APP', 'Desktop App Developer'),
        ('ANDROID_APP', 'Android App Developer'),
        ('IOS_APP', 'iOS App Developer'),
        ('WEB_APP', 'Web App Developer'),
        ('ML', 'Machine Learning'),
        ('AI', 'Artificial Intelligence')
]

SPECIALIZATION = [
        ('FED', 'Front End Developer'),
        ('BED', 'Back End Developer'),
        ('FSD', 'Full Stack Developer')
]

LEVEL = [
        ('BEG', 'Beginner'),
        ('EXP', 'Experienced'),
        ('PRO', 'Pro')
]

class Freelancer(User):
    ''' Model of Freelancer '''

    languages = models.CharField(max_length=50, choices=LANGUAGES)
    fields = models.CharField(max_length=50, choices=FIELDS)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION)
    level = models.CharField(max_length=20, choices=LEVEL)
    salary = models.IntegerField(validators=[max_value(1000), min_value(250)], default=250)
    github = models.URLField(max_length=100, default='')

    class Meta:
        verbose_name = 'Freelancer'
        verbose_name_plural = 'Freelancers'


class Employer(User):
    ''' Model of Employer '''
    company = models.CharField(max_length=100)
    company_website = models.URLField(max_length=500)

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

class Job(models.Model):
    ''' Model of the Job to be created by the employer '''
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    time_for_completion = models.IntegerField()

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

class Employee(models.Model):
    ''' Model of the employee for a job '''
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    languages = models.CharField(max_length=50, choices=LANGUAGES)
    fields = models.CharField(max_length=50, choices=FIELDS)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION)
    level = models.CharField(max_length=20, choices=LEVEL)
    salary = models.IntegerField(validators=[max_value(1000), min_value(250)])

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
