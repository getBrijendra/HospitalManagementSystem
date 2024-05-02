from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Patient, Doctor, Department, Appointment, PatientDiagnosis, PatientAllergy, PatientMedication, Diagnosis, Allergy, Medication, PatientDoctorAssignment, DoctorDepartmentAssignment #, PatientAppointmentAssignment



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('id', 'name')

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = ('id', 'name')

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ('id', 'name', 'dosage', 'frequency', 'notes')


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    #doctor = DoctorSerializer(read_only=True)  # Nested serializer for doctor data
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    #patient = PatientSerializer(read_only=True)  # Nested serializer for patient data
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    #department = DepartmentSerializer(read_only=True)  # Nested serializer for department data

    class Meta:
        model = Appointment
        fields = ('id', 'date', 'time', 'doctor', 'patient', 'department', 'status')




class PatientSerializer(serializers.ModelSerializer):
    diagnoses = DiagnosisSerializer(many=True, read_only=True)  # Assuming ManyToMany relationship
    allergies = AllergySerializer(many=True, read_only=True)  # Assuming ManyToMany relationship
    medications = MedicationSerializer(many=True, read_only=True)  # Assuming ManyToMany relationship
    #appointments = serializers.SerializerMethodField()  # Assuming ForeignKey relationship (optional)
    #appointments = AppointmentSerializer(many=True, read_only=True)  # Assuming ForeignKey relationship (optional)

    class Meta:
        model = Patient
        fields = ('id', 'name', 'age', 'gender', 'address', 'phone_number', 'email', 'diagnoses', 'allergies', 'medications')

    # def get_appointments(self, obj):
    #     # Implement logic to retrieve and serialize appointment data
    #     # (consider using nested serializers if needed)
    #     appointments = obj.appointments.all()
    #     # ... (serialize appointment data)
    #     serialized_appointment_data = []
    #     for appointment in appointments:
    #         serialized_appointment = {
    #             'id': appointment.id,
    #             'date': appointment.date,
    #             'time': appointment.time,
    #             'doctor': appointment.doctor,
    #             'patient': appointment.patient,
    #             'department': appointment.department,
    #             'status': appointment.status,
    #             # Add other fields as needed
    #         }
    #         serialized_appointment_data.append(serialized_appointment)

    #     return serialized_appointment_data



class DoctorSerializer(serializers.ModelSerializer):
    assigned_patients = serializers.SerializerMethodField()  # Assuming ManyToMany relationship

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'specialization', 'qualifications', 'experience_years', 'contact_details', 'assigned_patients')

    def get_assigned_patients(self, obj):
        # Implement logic to retrieve and serialize assigned patient data
        assigned_patients = obj.assigned_patients.all()
        # ... (serialize patient data)
        serialized_patient_data = []
        for patient in assigned_patients:
            serialized_patient = {
                'id': patient.id,
                'name': patient.name,
                'age': patient.age,
                'gender': patient.gender,
                'address': patient.address,
                'phone_number': patient.phone_number,
                # Add other fields as needed
            }
            serialized_patient_data.append(serialized_patient)
        return serialized_patient_data



class DepartmentSerializer(serializers.ModelSerializer):
    doctors = serializers.SerializerMethodField()  # Assuming ManyToMany relationship

    class Meta:
        model = Department
        fields = ('id', 'name', 'services_offered', 'doctors')

    def get_doctors(self, obj):
        # Implement logic to retrieve and serialize assigned doctor data
        doctors = obj.doctors.all()
        # Serialize each doctor
        serialized_doctors = []
        for doctor in doctors:
            serialized_doctor = {
                'id': doctor.id,
                'name': doctor.name,
                'specialization': doctor.specialization,
                'qualifications': doctor.qualifications,
                'experience_years': doctor.experience_years,
                'contact_details': doctor.contact_details,
                # Add other fields as needed
            }
            serialized_doctors.append(serialized_doctor)
        return serialized_doctors







class PatientDiagnosisSerializer(serializers.ModelSerializer):
    #patient = PatientSerializer(read_only=True)  # Nested serializer for patient data

    class Meta:
        model = PatientDiagnosis
        fields = ('id', 'patient', 'diagnosis', 'date')  # Adjust fields as needed


class PatientAllergySerializer(serializers.ModelSerializer):
    #patient = PatientSerializer(read_only=True)  # Nested serializer for patient data

    class Meta:
        model = PatientAllergy
        fields = ('id', 'patient', 'allergy', 'date')  # Adjust fields as needed


class PatientMedicationSerializer(serializers.ModelSerializer):
    #patient = PatientSerializer(read_only=True)  # Nested serializer for patient data

    class Meta:
        model = PatientMedication
        fields = ('id', 'patient', 'medication', 'date')  # Adjust fields as needed






class PatientDoctorAssignmentSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    #doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    #patient = PatientSerializer(read_only=True)  # Nested serializer for patient data

    class Meta:
        model = PatientDoctorAssignment
        fields = ('id', 'patient', 'doctor')  # Adjust fields as needed



class DoctorDepartmentAssignmentSerializer(serializers.ModelSerializer):
    #department = DepartmentSerializer(read_only=True)  # Nested serializer for department data
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    #doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = DoctorDepartmentAssignment
        fields = ('id', 'doctor', 'department')  # Adjust fields as needed



# class PatientAppointmentAssignmentSerializer(serializers.ModelSerializer):
#     #department = DepartmentSerializer(read_only=True)  # Nested serializer for department data
#     appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())
#     #doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

#     class Meta:
#         model = PatientAppointmentAssignment
#         fields = ('id', 'patient', 'appointment')  # Adjust fields as needed