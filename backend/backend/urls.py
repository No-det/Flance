from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from flance import api_views

router = routers.DefaultRouter()
router.register('freelancer', api_views.FreelancerView, 'freelancer')
router.register('employer', api_views.EmployerView, 'employer')
router.register('employee', api_views.EmployeeView, 'employee')
router.register('job', api_views.JobView, 'job')

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include('flance.urls')),
    path('apiViews/', include(router.urls)),
]
