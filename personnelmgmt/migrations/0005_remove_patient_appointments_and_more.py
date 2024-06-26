# Generated by Django 4.2.11 on 2024-04-30 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnelmgmt', '0004_remove_patient_appointments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='appointments',
        ),
        migrations.DeleteModel(
            name='PatientAppointmentAssignment',
        ),
        migrations.AddField(
            model_name='patient',
            name='appointments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_patients', to='personnelmgmt.appointment'),
        ),
    ]
