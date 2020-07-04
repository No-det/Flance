from django.contrib import admin
from .models import Freelancer, Project
from .models import Employer, Employee, Job

admin.site.register(Freelancer)
admin.site.register(Employer)
admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Job)
