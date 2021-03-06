# Generated by Django 4.0.2 on 2022-02-20 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('company_name', models.CharField(max_length=500)),
                ('expected_salary', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('min_year_of_experience', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('college_grads_batch', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('job_type', models.TextField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Contract', 'Contract'), ('Internship', 'Internship'), ('Volunteer', 'Volunteer'), ('Temporary', 'Temporary')])),
                ('degree', models.CharField(blank=True, max_length=1000, null=True)),
                ('roles_and_responsibilities', models.TextField()),
                ('skills', models.TextField()),
                ('true_job_link', models.TextField()),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Job',
            },
        ),
    ]
