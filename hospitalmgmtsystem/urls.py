"""
URL configuration for hospitalmgmtsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
#from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from personnelmgmt import views

schema_view = get_schema_view(
    openapi.Info(
        title="Hospital Management System",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'diagnosis', views.DiagnosisViewSet)
router.register(r'allergy', views.AllergyViewSet)
router.register(r'medication', views.MedicationViewSet)
router.register(r'patientdiagnosis', views.PatientDiagnosisViewSet)
router.register(r'patientallergy', views.PatientAllergyViewSet)
router.register(r'patientmedication', views.PatientMedicationViewSet)
router.register(r'patientdoctorassignment', views.PatientDoctorAssignmentViewSet)
router.register(r'doctordepartmentassignment', views.DoctorDepartmentAssignmentViewSet)
#router.register(r'patientappointmentassignment', views.PatientAppointmentAssignmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('', include("personnelmgmt.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),

]
