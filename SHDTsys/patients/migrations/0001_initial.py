# Generated by Django 5.0.3 on 2024-04-03 11:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_auth', '0006_user_role_delete_userdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('type', models.CharField(blank=True, max_length=255)),
                ('caused_by', models.TextField(blank=True, max_length=255)),
                ('Reaction', models.TextField(blank=True, max_length=255)),
                ('severity', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Extreme', 'Extreme')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pics/')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('date_of_birth', models.DateField(blank=True)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('NA', 'Prefer not to say')], max_length=10)),
                ('emergency_contact_info', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_medical_history',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('procedure_name', models.CharField(blank=True, max_length=60)),
                ('procedure_date', models.DateField(blank=True, null=True)),
                ('operator_name', models.CharField(blank=True, max_length=60)),
                ('procedure_hospital', models.CharField(blank=True, max_length=255)),
                ('procedure_report', models.FileField(blank=True, null=True, upload_to='')),
                ('smoking_status', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Extreme', 'Extreme')], max_length=10)),
                ('alcohol_status', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Extreme', 'Extreme')], max_length=10)),
                ('illegal_items_status', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Extreme', 'Extreme')], max_length=10)),
                ('other_social_factors', models.TextField(blank=True, max_length=255)),
                ('relative_name', models.CharField(blank=True, max_length=100)),
                ('relationship', models.CharField(blank=True, max_length=60)),
                ('relative_medical_condition', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('target_disease', models.CharField(blank=True, max_length=255)),
                ('recommended_doses', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.CharField(max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('reason_for_use', models.TextField(blank=True, max_length=255)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.medication')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_date', models.DateField(blank=True, null=True)),
                ('dose_number', models.PositiveIntegerField(blank=True, null=True)),
                ('next_dose_due', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, max_length=255)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.vaccine')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onset_date', models.DateField(blank=True, null=True)),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.allergy')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
            options={
                'unique_together': {('patient', 'allergy')},
            },
        ),
    ]
