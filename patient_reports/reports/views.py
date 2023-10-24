# reports/views.py

from django.shortcuts import render, redirect, HttpResponse
from .models import PatientReport
from .forms import PatientReportForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'reports/login.html')
def home(request):
    return render(request, 'reports/index.html')

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
    return render(request, 'view_report.html', {'report': report})


# Create your views here.
# @login_required(login_url='login')


# def SignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')

#         if pass1!=pass2:
#             return HttpResponse("Your password and confrom password are not Same!!")
#         else:

#             my_user=User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login')
        



#     return render (request,'signup.html')

# def Login(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('pass')
#         user=authenticate(request,username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponse ("Username or Password is incorrect!!!")

#     return render (request,'login.html')

# def LogoutPage(request):
#     logout(request)
#     return redirect('login')