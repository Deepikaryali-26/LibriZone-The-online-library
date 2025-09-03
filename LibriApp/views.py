from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from LibriApp.forms import BookForm
from LibriApp.forms import RegistrationForm
from django.contrib.auth import logout,authenticate,login
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from LibriZone import settings
from django.contrib import messages
from .models import Book

# Create your views here.
def register(request):
    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    return render(request,'register.html',{'form':form})

def display(request):
    data=Register.objects.all()
    return render(request,'display.html',{'info':data})

def login_view(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['psw']
        u=authenticate( request,username=username,password=password)
        if u:
            login(request,u)
            # return HttpResponse("<h2>Authenticated User!</h2>")
            return redirect('/home')
        else:
          messages.error(request,'Invalid username or password.')
        return render(request, 'login.html',{})
    else:
        return render(request, 'login.html', {})

def signout(request):
    logout(request)
    return redirect('/home')

def Contact(request):
    return render(request,'Contact.html',{})

def home(request):
    return render(request,'home.html',{})


@login_required
def upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            return redirect('/explore')
    else:
        form = BookForm()
    return render(request, 'upload.html', {'form': form})


def explore(request):
    categories = {
        'Education': Book.objects.filter(category='Education'),
        'Fiction': Book.objects.filter(category='Fiction'),
        'Thriller': Book.objects.filter(category='Thriller'),
        'Mythology': Book.objects.filter(category='Mythology'),
        'Comics': Book.objects.filter(category='Comics'),
    }
    return render(request, 'explore.html', {'categories': categories})

def read_book(request):
    book = Book.objects.all()
    return render(request, 'read_book.html', {'book': book})