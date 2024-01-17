from django.shortcuts import render
from .forms import mobileformtask,moviereviewform,commentform,registerform
from django.http import HttpResponse
from .models import mobiletask,movie,comments
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


# Create your views here.
def insertform(request):
    form = mobileformtask()
    if request.method == 'POST' and request._files:
        form = mobileformtask(request.POST,request._files)
        if form.is_valid():
            form.save()
            return HttpResponse('data inserted successfully')
    return render(request,'insertimage.html',{'form':form})

def displayproduct(request):
    data = mobiletask.objects.all()
    return render(request,'display.html',{'data':data})

def detailsview(request,id):
    data = mobiletask.objects.get(id=id)
    return render(request,'details.html',{'data':data})



def movieview(request):
    form = moviereviewform()
    if request.method=='POST' and request._files:
        form=moviereviewform(request.POST,request._files)
        if form.is_valid():
            form.save()
            return HttpResponse('movie review inserted successfully')
    return render(request,'movie.html',{'form':form})

def displayall(request):
    data = movie.objects.all()
    return render(request,'home.html',{'data':data})

@login_required(login_url='/login/')
def displayone(request,id):
    data=movie.objects.get(id=id)
    form = commentform(initial={'review':id})
    comment = comments.objects.filter(review_id=id)
    if request.method == 'POST':
        form1=commentform(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request,'single.html',{'data':data,'form':form,'comment':comment}) 

def homepageview(request):
    return render(request,'homepage.html')

# def registerview(request):
#     form=registerform
#     if request.method == 'POST':
#         form = registerform(request.POST)
#         if form.is_valid():
#             form=form.save(commit=False)
#             password=form.password
#             form.password = make_password(password)
#             form.save()
#             return HttpResponse('register successfully')
#     return render(request,'register.html',{'form':form})
def registerview(request):
    form = registerform
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            password = form.password
            form.password = make_password(password)
            form.save()
            return HttpResponse('registered successfully')
    return render(request,'register.html',{'form':form})


def loginview(request):
    form = AuthenticationForm
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            data = movie.objects.all()
            return render(request,'home.html',{'data':data})
        else:
            form = registerform
            if request.method == 'POST':
                form = registerform(request.POST)
                if form.is_valid():
                   form=form.save(commit=False)
                   password=form.password
                   form.password = make_password(password)
                   form.save()
                   return HttpResponse('register successfully')
            return render(request,'register.html',{'form':form})
    return render(request,'login.html',{'form':form})

@login_required(login_url='/login/')
def logoutview(request):
    logout(request)
    return HttpResponse('logout successfull')


