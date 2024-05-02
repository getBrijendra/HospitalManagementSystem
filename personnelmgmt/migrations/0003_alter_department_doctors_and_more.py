# Generated by Django 4.2.11 on 2024-04-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnelmgmt', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='doctors',
            field=models.ManyToManyField(null=True, through='personnelmgmt.DoctorDepartmentAssignment', to='personnelmgmt.doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='assigned_patients',
            field=models.ManyToManyField(null=True, through='personnelmgmt.PatientDoctorAssignment', to='personnelmgmt.patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=models.ManyToManyField(null=True, through='personnelmgmt.PatientAllergy', to='personnelmgmt.allergy'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='diagnoses',
            field=models.ManyToManyField(null=True, through='personnelmgmt.PatientDiagnosis', to='personnelmgmt.diagnosis'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='medications',
            field=models.ManyToManyField(null=True, through='personnelmgmt.PatientMedication', to='personnelmgmt.medication'),
        ),
    ]