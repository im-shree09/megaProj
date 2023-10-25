# Generated by Django 4.2.6 on 2023-10-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientreport',
            name='id',
        ),
        migrations.AddField(
            model_name='patientreport',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patientreport',
            name='medical_history',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='patientreport',
            name='mobile_number',
            field=models.CharField(default='', max_length=15, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='patientreport',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1),
        ),
    ]
