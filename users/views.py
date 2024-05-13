
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserForm
from users.models import Users
from django.contrib.auth.decorators import login_required
from student.models import Student
from book.models import Book , Author
from borrowing.models import Borrowing
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from django.contrib.auth import update_session_auth_hash


@login_required
def home(req):
    x = {
        'user' : Users.objects.get(info__username=req.user.username),
        'count_student' : Student.objects.count(),
        'count_book' : Book.objects.count(),
        'count_author' : Author.objects.count(),
        'count_borrowing' : Borrowing.objects.count()
    }

    return render(req,'users/index.html',x)

def connecte(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        authi = authenticate(req, username=username, password=password)
        user = Users.objects.filter(info__username=username)
        if authi is not None and user[0].active == True :
            login(req, authi)
            return redirect('home')
        elif authi is None :
            messages.error(req, 'Username ou password incorrect.')
        else:
            messages.info(req, "Votre compte est desactive par l'administrateur <br> Merci de contacte pour l'active.")

    return render(req, 'users/login.html')

def deconecte(req):
    logout(req)
    return redirect('login')  

def signup(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            user=form.save()
            Users(info=user).save()
            return redirect('login') 
    else:
        form = UserForm()
    return render(req, 'users/signup.html', {'form': form})

@login_required
def profile(req):
    user=Users.objects.get(info__username=req.user.username)
    form = UserForm(instance=user.info)
    if req.method == 'POST':
        form = UserForm(req.POST, instance=user.info)
        if form.is_valid():
            form.save()
            user = authenticate(req, username=req.user.username, password=req.user.password)
            login(req, user)
            return redirect('home') 
    return render(req, 'users/profile.html', {'form': form,'user':user  })

def reset_password(req):
    if req.method == 'POST':
        email=req.POST['email']
        user = Users.objects.filter(info__email=email).first()
        if user :
            mail =_email(user,req)

            if mail:
                messages.info(req, "Email sent successfully.")
            else : 
                messages.error(req, "Failed to send email.")
        else:
            messages.error(req, "this email not existe .")
    return render(req,'users/reset-password.html')
def get_current_host(request):
    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol, host=host)

def _email(user,request):
    token = get_random_string(40)
    expire_date = datetime.now() + timedelta(minutes=30)
    user.reset_password_token = token
    user.reset_password_expire = expire_date
    user.save()

    host = get_current_host(request)
    link = "http://localhost:8000/accounts/update-password/{token}".format(token=token)
    subject = 'Réinitialisation de mot de passe'
    message = f'Pour reinitialiser votre mot de passe,<br> cliquez sur ce<a href="{link}">lien</a>'.format(link=link)
    try:
        send_mail(subject, message, 'mailtrap@demomailtrap.com', [user.info.email])
        return True
    except :
        return False


def update_password(req, token):
    try:
        user = Users.objects.get(reset_password_token=token)
    except Users.DoesNotExist:
        return redirect('login')  


    #if user.reset_password_expire <= datetime.now():
     #   return redirect('login') 
    if req.method=='POST':
        password1 = req.POST.get('password1')
        password2= req.POST.get('password2')
        if password1!=password2 and len(password1) <6 :
            messages.info(req,'Verifier votre password!')
        else:
            user=user.info
            user.set_password(password1)
            user.save()
            update_session_auth_hash(req, user)
            
            messages.info(req,'Votre  mot de passe modefier avec success!')
            return redirect('login')
    
    return render(req, 'users/update_password.html')
