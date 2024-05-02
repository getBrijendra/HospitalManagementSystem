from django.db import models

# Create your models here.


class Patient(models.Model):

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    # Medical History (consider using ManyToMany relationships)
    diagnoses = models.ManyToManyField('Diagnosis', through='PatientDiagnosis', null=True)  # Optional: using ManyToManyField
    allergies = models.ManyToManyField('Allergy', through='PatientAllergy', null=True)  # Optional: using ManyToManyField
    medications = models.ManyToManyField('Medication', through='PatientMedication', null=True)  # Optional: using ManyToManyField

    # Appointment Records (consider using a ForeignKey)
    #appointments = models.ForeignKey('Appointment', on_delete=models.CASCADE, null=True, blank=True, related_name='assigned_patients')  # Optional: using ForeignKey
    #appointments = models.ManyToManyField('Appointment', through='PatientAppointmentAssignment', null=True, related_name='assigned_patients')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=100)
    qualifications = models.TextField()
    experience_years = models.PositiveIntegerField()
    contact_details = models.CharField(max_length=255)

    # Availability Schedule (consider using a separate model or custom field)
    # You can explore options like storing availability as time slots or using a calendar library

    # Assigned Patients (consider using ManyToMany relationship)
    assigned_patients = models.ManyToManyField('Patient', through='PatientDoctorAssignment', null=True)  # Optional: using ManyToManyField

    def __str__(self):
        return self.name



class Department(models.Model):
    name = models.CharField(max_length=255)
    services_offered = models.TextField()

    # Assigned Doctors (consider using ManyToMany relationship)
    doctors = models.ManyToManyField('Doctor', through='DoctorDepartmentAssignment', null=True)  # Optional: using ManyToManyField

    def __str__(self):
        return self.name



class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # Doctor assigned to the appointment
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # Patient for the appointment
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # Department associated with the appointment
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed')))
    # Additional fields (optional)
    # - notes (TextField): To store additional details about the appointment

    def __str__(self):
        return f"{self.patient.name} - {self.date} ({self.status})"




class Diagnosis(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Allergy(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)  # Adjust field type as needed
    frequency = models.CharField(max_length=100)  # Adjust field type as needed
    notes = models.TextField(blank=True)  # Optional

    def __str__(self):
        return f"{self.name} ({self.dosage}, {self.frequency})"




class PatientDiagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)  # Optional: To track diagnosis date

    def __str__(self):
        return f"{self.patient.name} - {self.diagnosis.name}"

        

class PatientAllergy (models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)  # Optional: To track diagnosis date

    def __str__(self):
        return f"{self.patient.name} - {self.diagnosis.name}"



class PatientMedication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)  # Optional: To track diagnosis date

    def __str__(self):
        return f"{self.patient.name} - {self.diagnosis.name}"




class PatientDoctorAssignment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('patient', 'doctor')  # Ensures a patient is assigned to a doctor only once

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"




class DoctorDepartmentAssignment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('doctor', 'department')  # Ensures a doctor belongs to a department only once

    def __str__(self):
        return f"{self.doctor.name} - {self.department.name}"


# class PatientAppointmentAssignment(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('patient', 'appointment')  # Ensures a patient belongs to a appointment only once

#     def __str__(self):
#         return f"{self.patient.name} - {self.appointment.name}"