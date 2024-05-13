from django.shortcuts import render,redirect
from student.forms import StudentForm
from django.db.models import Q
from student.models import Student
from django.contrib.auth.decorators import login_required

from users.models import Users
# Create your views here.
@login_required
def index (req):
    data = Student.objects.all()
    user=Users.objects.get(info__username=req.user.username)
    x={
        "students" : data,
        'user' : user
    }
    if req.method=='GET' and req.GET.get('search') :
        mc=req.GET.get('search')
        data=Student.objects.filter(Q(name__contains=mc) | Q(surname__contains=mc))
        x['search']=mc
        x['students']=data
    return render(req,'student/index.html',x)

@login_required
def create(req):
    form = StudentForm() 
    user=Users.objects.get(info__username=req.user.username)
    if req.method == 'POST':
        form = StudentForm(req.POST) 
        if form.is_valid():
            form.save()
            return redirect('student')
    return render(req,'student/new.html', {'form' : form,'user':user })

@login_required
def edit(req,id):
    user=Users.objects.get(info__username=req.user.username)
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if req.method == 'POST':
        form = StudentForm(req.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student') 
    return render(req, 'student/edit.html', {'form': form,'user':user ,'student' : student })

@login_required
def delete (req , id):
    Student.objects.get(id=id).delete()
    return redirect('student')
