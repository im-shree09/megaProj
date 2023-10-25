# reports/forms.py

from django import forms
from .models import PatientReport

class PatientReportForm(forms.ModelForm):
    class Meta:
        model = PatientReport
        fields = ['patient_name','mobile_number', 'age', 'sex', 'medical_history', 'report']
