from django.contrib import admin
from django.urls import path, include
from rest_framework import routers                    # add this
from flance import api_views

router = routers.DefaultRouter()                      # add this
router.register('freelancer', api_views.FreelancerView, 'freelancer')
router.register('employer', api_views.EmployerView, 'employer')
router.register('employee', api_views.EmployeeView, 'employee')
router.register('job', api_views.JobView, 'job')

urlpatterns = [
    path('', include('flance.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
