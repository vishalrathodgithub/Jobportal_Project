# Generated by Django 2.2.7 on 2019-12-05 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MECHJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_company', models.CharField(max_length=30)),
                ('job_title', models.CharField(max_length=30)),
                ('job_description', models.TextField()),
                ('job_designation', models.CharField(max_length=30)),
                ('job_experience', models.FloatField()),
                ('job_package', models.FloatField()),
                ('job_position', models.IntegerField()),
                ('job_date_from', models.DateField()),
                ('job_date_to', models.DateField()),
                ('job_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Firstapp.Address')),
            ],
        ),
        migrations.CreateModel(
            name='ITJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_company', models.CharField(max_length=30)),
                ('job_title', models.CharField(max_length=30)),
                ('job_description', models.TextField()),
                ('job_designation', models.CharField(max_length=30)),
                ('job_experience', models.FloatField()),
                ('job_package', models.FloatField()),
                ('job_position', models.IntegerField()),
                ('job_date_from', models.DateField()),
                ('job_date_to', models.DateField()),
                ('job_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Firstapp.Address')),
            ],
        ),
        migrations.CreateModel(
            name='CIVILJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_company', models.CharField(max_length=30)),
                ('job_title', models.CharField(max_length=30)),
                ('job_description', models.TextField()),
                ('job_designation', models.CharField(max_length=30)),
                ('job_experience', models.FloatField()),
                ('job_package', models.FloatField()),
                ('job_position', models.IntegerField()),
                ('job_date_from', models.DateField()),
                ('job_date_to', models.DateField()),
                ('job_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Firstapp.Address')),
            ],
        ),
    ]