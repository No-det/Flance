from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
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

# User is the base model

class User(AbstractUser):
    is_freelancer = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

class Freelancer(models.Model):
    ''' Model of Freelancer '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='freelancer')
    dp = models.ImageField('Profile Pic', blank=True)
    languages = models.CharField('Languages', max_length=50, choices=LANGUAGES)
    fields = models.CharField('Fields', max_length=50, choices=FIELDS)
    specialization = models.CharField('Specialization', max_length=50, choices=SPECIALIZATION)
    level = models.CharField('Level', max_length=20, choices=LEVEL)
    salary = models.IntegerField('Salary', validators=[max_value(1000), min_value(250)], default=250)

    class Meta:
        verbose_name = 'Freelancer'
        verbose_name_plural = 'Freelancers'


class Employer(models.Model):
    ''' Model of Employer '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employer')
    dp = models.ImageField('Profile Pic', blank=True)
    company = models.CharField('Company', max_length=100)
    location = models.CharField('Location', max_length=30)
    website = models.URLField('Website', blank=True)

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'




class Job(models.Model):
    ''' Model of the Job to be created by the employer '''
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=50)
    mode = models.CharField('Mode', max_length=5, choices=[('ftime', 'Full-Time'), ('ptime', 'Part-Time')])
    etc = models.PositiveIntegerField('Estimated time for completion (Hrs)', validators=[max_value(2000)])

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class Employee(models.Model):
    ''' Model of the employee for a job '''
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    languages = models.CharField('Languages', max_length=50, choices=LANGUAGES)
    fields = models.CharField('Fields', max_length=50, choices=FIELDS)
    specialization = models.CharField('Specialization', max_length=50, choices=SPECIALIZATION)
    level = models.CharField('Level', max_length=20, choices=LEVEL)
    salary = models.IntegerField('Salary', validators=[max_value(1000), min_value(250)], default=250)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
