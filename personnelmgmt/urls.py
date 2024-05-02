from django.urls import include, path
from rest_framework import routers

from personnelmgmt import views

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

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]