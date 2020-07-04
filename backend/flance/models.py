from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator as max_value
from django.core.validators import MinValueValidator as min_value
from .opt_models import (
    LANGUAGES, SPECIALIZATION, FIELDS, SIDE, LEVEL
)


class User(AbstractUser):
    is_freelancer = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


class Freelancer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='freelancer')
    dp = models.ImageField('Profile Pic', blank=True)
    languages = models.CharField('Languages', max_length=50, choices=LANGUAGES)
    specialization = models.CharField('Specialization', max_length=50, choices=SPECIALIZATION)
    fields = models.CharField('Fields', max_length=50, choices=FIELDS)
    side = models.CharField('Side', max_length=50, choices=SIDE)
    level = models.CharField('Level', max_length=20, choices=LEVEL)
    salary = models.IntegerField('Salary', validators=[max_value(1000), min_value(250)], default=250)

    class Meta:
        verbose_name = 'Freelancer'
        verbose_name_plural = 'Freelancers'


class Employer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employer')
    dp = models.ImageField('Profile Pic', blank=True)
    company = models.CharField('Company', max_length=100)
    location = models.CharField('Location', max_length=30)
    website = models.URLField('Website', blank=True)

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'




class Project(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=50)
    tech = models.CharField('Technology used', max_length=50)
    desc = models.CharField('Description', max_length=200)
    link = models.URLField('Project URL')
    ss = models.ImageField('ScreenShot', blank=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Job(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=50)
    mode = models.CharField('Mode', max_length=5, choices=[('ftime', 'Full-Time'), ('ptime', 'Part-Time')])
    etc = models.PositiveIntegerField('Estimated time for completion (Hrs)', validators=[max_value(2000)])

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class Employee(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    languages = models.CharField('Languages', max_length=50, choices=LANGUAGES)
    specialization = models.CharField('Specialization', max_length=50, choices=SPECIALIZATION)
    fields = models.CharField('Fields', max_length=50, choices=FIELDS)
    side = models.CharField('Side', max_length=50, choices=SIDE)
    level = models.CharField('Level', max_length=20, choices=LEVEL)
    salary = models.IntegerField('Salary', validators=[max_value(1000), min_value(250)], default=250)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
