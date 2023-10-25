# reports/models.py

from django.db import models

class PatientReport(models.Model):
    patient_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, primary_key=True, default='')
    # age = models.IntegerField()
    age = models.IntegerField(default=0) 
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='F')
    medical_history = models.TextField(default=' ')
    report = models.FileField(upload_to='patient_reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name
