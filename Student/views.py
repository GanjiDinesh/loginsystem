from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Student.models import Student, City, Course


# Create your views here.
@login_required
def home(request):
    return redirect('displaystudent')

@login_required
def displaystudent(request):
    return render(request,'displaystudent.html',{'students':Student.objects.all()})

@login_required
def addstudent(request):
    cities = City.objects.all()
    course = Course.objects.all()
    return render(request, 'addstudent.html', {'cities': cities, 'course': course})


def readstudentdata(request):
    s = Student()
    s.fname = request.POST['tbfname']
    s.lname = request.POST['tblname']
    s.mobile = request.POST['tbmobile']
    s.email = request.POST['tbemail']
    s.city_name =City.objects.get(city_name= request.POST['ddlcity'])
    s.course_name = Course.objects.get(course_name=request.POST['ddlcourse'])
    s.save()
    return redirect('displaystudent')


def updatestudent(request,id):
    s = Student.objects.get(id=id)
    cities = City.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        s.fname = request.POST['tbfname']
        s.lname = request.POST['tblname']
        s.mobile = request.POST['tbmobile']
        s.email = request.POST['tbemail']
        s.city_name = City.objects.get(city_name=request.POST['ddlcity'])
        s.course_name = Course.objects.get(course_name=request.POST['ddlcourse'])
        s.save()
        return redirect('displaystudent')
    return render(request, 'updatestudent.html', {'data': s,'cities': cities, 'course': course})


def deletestudent(request,id):
    b1 = Student.objects.get(id=id)
    b1.delete()
    return redirect('displaystudent')

