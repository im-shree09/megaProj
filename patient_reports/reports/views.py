# reports/views.py

from django.shortcuts import render, redirect
from .models import PatientReport
from .forms import PatientReportForm

def report_list(request):
    reports = PatientReport.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

def upload_report(request):
    if request.method == 'POST':
        form = PatientReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = PatientReportForm()
    return render(request, 'reports/upload_report.html', {'form': form})

def view_report(request, pk):
    report = PatientReport.objects.get(pk=pk)
    return render(request, 'reports/view_report.html', {'report': report})
