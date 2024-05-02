from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from personnelmgmt.serializers import GroupSerializer, UserSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # Optional: Authentication

from .models import Patient, Doctor, Department, Appointment, Diagnosis, Allergy, Medication, PatientDiagnosis, PatientAllergy, PatientMedication, PatientDoctorAssignment, DoctorDepartmentAssignment #, PatientAppointmentAssignment
from .serializers import PatientSerializer, DoctorSerializer, DepartmentSerializer, AppointmentSerializer, DiagnosisSerializer, AllergySerializer, MedicationSerializer, PatientDiagnosisSerializer, PatientAllergySerializer, PatientMedicationSerializer, PatientDoctorAssignmentSerializer, DoctorDepartmentAssignmentSerializer#, PatientAppointmentAssignmentSerializer
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]




class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('id')
    serializer_class = PatientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'phone_number', 'email', 'address']
    permission_classes = [IsAuthenticated]  # Optional: Authentication


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'specialization', 'qualifications', 'contact_details']
    permission_classes = [IsAuthenticated]  # Optional: Authentication


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'services_offered']
    permission_classes = [IsAuthenticated]  # Optional: Authentication




class AppointmentFilter(filters.FilterSet):
    doctor_name = filters.CharFilter(field_name='doctor__name', lookup_expr='icontains')
    patient_name = filters.CharFilter(field_name='patient__name', lookup_expr='icontains')
    department_name = filters.CharFilter(field_name='department__name', lookup_expr='icontains')
    status = filters.CharFilter(field_name='status', lookup_expr='icontains')

    class Meta:
        model = Appointment
        fields = ['doctor_name', 'patient_name', 'department_name', 'status']

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('id')
    serializer_class = AppointmentSerializer
    # filter_backends = [SearchFilter]
    # search_fields = ['doctor', 'patient', 'department', 'status']
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_class = AppointmentFilter
    search_fields = ['doctor__name', 'patient__name', 'department__name', 'status']
    permission_classes = [IsAuthenticated]  # Optional: Authentication



class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated] 


class AllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    permission_classes = [IsAuthenticated] 



class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated] 



class PatientDiagnosisViewSet(viewsets.ModelViewSet):
    queryset = PatientDiagnosis.objects.all()
    serializer_class = PatientDiagnosisSerializer
    permission_classes = [IsAuthenticated] 



class PatientAllergyViewSet(viewsets.ModelViewSet):
    queryset = PatientAllergy.objects.all()
    serializer_class = PatientAllergySerializer
    permission_classes = [IsAuthenticated] 



class PatientMedicationViewSet(viewsets.ModelViewSet):
    queryset = PatientMedication.objects.all()
    serializer_class = PatientMedicationSerializer
    permission_classes = [IsAuthenticated] 



class PatientDoctorAssignmentViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorAssignment.objects.all()
    serializer_class = PatientDoctorAssignmentSerializer
    permission_classes = [IsAuthenticated] 



class DoctorDepartmentAssignmentViewSet(viewsets.ModelViewSet):
    queryset = DoctorDepartmentAssignment.objects.all()
    serializer_class = DoctorDepartmentAssignmentSerializer
    permission_classes = [IsAuthenticated] 


# class PatientAppointmentAssignmentViewSet(viewsets.ModelViewSet):
#     queryset = PatientAppointmentAssignment.objects.all()
#     serializer_class = PatientAppointmentAssignmentSerializer
#     permission_classes = [IsAuthenticated] 

