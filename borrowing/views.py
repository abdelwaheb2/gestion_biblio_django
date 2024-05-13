from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from borrowing.forms import BorrowingForm
from users.models import Users
from .models import Borrowing
from book.models import Book
from student.models import Student

# Create your views here.
@login_required
def index (req):
    user=Users.objects.get(info__username=req.user.username)
    data = Borrowing.objects.all()
    books =Book.objects.all()
    x={
        "borrowings" : data,
        'user':user,
        'books':books
    }
    if req.method=='GET' and (req.GET.get('search') or req.GET.get('book')) :
        mc=req.GET['search']
        book=req.GET['book']
        data=data.filter(Q(student_id__name__contains=mc) | Q(student_id__surname__contains=mc))
        print(book)
        if book!='all' :
            data=data.filter(book_id__title=book)
            x['book']=book
        x['search']=mc
        x['borrowings']=data
    return render(req,'borrowing/index.html',x)

@login_required
def create(req):
    user=Users.objects.get(info__username=req.user.username)
    form = BorrowingForm()
    books =Book.objects.all()
    students=Student.objects.all()
    if req.method == 'POST':
        form = BorrowingForm(req.POST)
        id_b=req.POST['book']
        id_s=req.POST['student']
        print(id_b)
        if form.is_valid() and id_b!="0" and id_s!="0":
            date =form.data.get('date_borrowing')
            returned = form.data.get('book_returned') == 'on'
            book = Book.objects.get(id=int(id_b))
            student = Student.objects.get(id=int(id_s))
            print(book)
            Borrowing.objects.create(book_id=book,student_id=student,date_borrowing=date,book_returned=returned)
            return redirect('borrowing')
    return render(req,'borrowing/new.html', {'form' : form ,'user':user,'books':books,'students':students})

@login_required
def edit(req,id):
    borrowing = Borrowing.objects.get(id=id)
    user=Users.objects.get(info__username=req.user.username)
    books =Book.objects.all()
    students=Student.objects.all()
    form = BorrowingForm(instance=borrowing)
    if req.method == 'POST':
        form = BorrowingForm(req.POST, instance=borrowing)
        if form.is_valid():
            form.save()
            return redirect('borrowing') 
    x={
        'form' : form ,
        'students' : students,
        'books': books,
        'borrowing':borrowing,
        'user':user
    }
    return render(req, 'borrowing/edit.html' , x)

@login_required
def delete (req , id):
    Borrowing.objects.get(id=id).delete()
    return redirect('borrowing')
