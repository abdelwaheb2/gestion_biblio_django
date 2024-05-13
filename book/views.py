from django.shortcuts import render,redirect
from django.db.models import Q
from book.formes import AuthorForm, BookForm
from users.models import Users
from .models import Book , Author ,Book_Author
from django.contrib.auth.decorators import login_required




# Create your views here.
#views books--------------------------------------
@login_required
def index_book (req):
    books = Book.objects.all()
    data=[]
    for book in books:
        authors = Book_Author.objects.filter(book_id=book.id)#.values_list('author_id')
        book_data = {
            'id': book.id,
            'title': book.title,
            'authors': authors
        }
        data.append(book_data)
    user=Users.objects.get(info__username=req.user.username)
    x={
        "user" : user,
        "books" : data,
    }
    if req.method=='GET' and req.GET.get('search') :
        mc=req.GET.get('search')
        data=Book.objects.filter(title__contains=mc)
        x['search']=mc
        x['books']=data
    return render(req,'book/index.html',x)

@login_required
def create_book(req):
    user=Users.objects.get(info__username=req.user.username)
    form = BookForm()
    authors = Author.objects.all()

    if req.method == 'POST':
        form = BookForm(req.POST)
        authors=req.POST.get('authors').split(',')
        authors.pop(0)
        if form.is_valid() :
            newbook=form.save()
            for i in authors:
                author = Author.objects.get(id=int(i))
                book_author = Book_Author(book_id=newbook, author_id=author)
                book_author.save()
            return redirect('book')
    return render(req,'book/new.html', {'form' : form , 'authors' : authors , 'user' : user })

@login_required
def edit_book(req,id):
    user=Users.objects.get(info__username=req.user.username)
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)
    authors = Author.objects.all()
    book_author = Book_Author.objects.filter(book_id=id)
    if req.method == 'POST':
        author_id = int(req.POST.get('author'))
        form = BookForm(req.POST, instance=book)
        if form.is_valid() and author_id !=0:
            newbook=form.save()
            author = Author.objects.get(id=author_id)
            if(author != book_author.author_id):
                book_author.author_id=author
                book_author.save()
            return redirect('book') 
    return render(req, 'book/edit.html', {'authours_c':book_author ,'user':user,'form': form, 'book': book, 'authors' : authors })

@login_required
def delete_book (req , id):
    Book.objects.get(id=id).delete()
    return redirect('author')
#views author-------------------------------------

@login_required
def index_author (req):
    data = Author.objects.all()
    user=Users.objects.get(info__username=req.user.username)
    x={
        "authors" : data,
        'user':user
    }
    if req.method=='GET' and req.GET.get('search') :
        mc=req.GET.get('search')
        data=Author.objects.filter(Q(name__contains=mc) | Q(surname__contains=mc))
        x['search']=mc
        x['authors']=data
    return render(req,'author/index.html',x)

@login_required
def create_author(req):
    user=Users.objects.get(info__username=req.user.username)
    form = AuthorForm() 
    if req.method == 'POST':
        form = AuthorForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('author')
    return render(req,'author/new.html', {'form' : form , 'user':user })

@login_required
def edit_author(req,id):
    user=Users.objects.get(info__username=req.user.username)
    author = Author.objects.get(id=id)
    form = AuthorForm(instance=author)
    if req.method == 'POST':
        form = AuthorForm(req.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author') 
    return render(req, 'author/edit.html', {'form': form, 'author' : author , 'user':user })

@login_required
def delete_author (req , id):
    Author.objects.get(id=id).delete()
    return redirect('author')
