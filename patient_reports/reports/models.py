# reports/models.py

from django.db import models

class PatientReport(models.Model):
    patient_name = models.CharField(max_length=100)
    report = models.FileField(upload_to='patient_reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name
