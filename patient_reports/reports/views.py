# reports/views.py

from django.shortcuts import render, redirect, HttpResponse
from .models import PatientReport
from .forms import PatientReportForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'reports/land.html')

def dash(request):
    return render(request, 'dashboard.html')

def docdash(request):
    return render(request, 'docdash.html')


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
    return render(request, 'upload_report.html', {'form': form})

def view_report(request, pk):
    report = PatientReport.objects.get(pk=pk)
    return render(request, 'details.html', {'report': report})


def lp(request, pk):
    report = PatientReport.objects.get(pk=pk)
    return render(request, 'profile.html', {'report': report})

# Create your views here.
@login_required(login_url='loginn')

# def mk(request):
#     # report = PatientReport.objects.get()
#     return render(request, 'list.html')

def mk(request):
    reports = PatientReport.objects.all()
    # print(reports)
    return render(request, 'reports/list.html', {'reports': reports})


def loginn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('mk')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('loginn')
    return render (request,'singup.html')

def doctor_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('docdash')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'doctor_login.html')

def doctor_register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('doctor_login')
    return render (request,'doctor_register.html')



def LogoutPage(request):
    logout(request)
    return redirect('loginn')