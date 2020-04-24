from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import SignupUser,PostData
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url="/myapp/login")
def home(request):
    if request.method == "GET":
        profiles = User.objects.all()
        print(profiles)
        return render(request,'registration/home.html',{'profiles':profiles})


def signup_view(request):
    if request.method =="POST":
        print("request recieved")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("form valid")
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request,'registration/signup.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('login')

def ShowUserPage(request,usp_id):
    profile = User.objects.get(id=usp_id)
    print("user name is ",profile)
    return render(request,"registration/user-profile.html",{"profile":profile})

def posts(request):
    if request.method == "POST":
        posts_user = PostData()
        postTitle = request.POST['postTitle']
        print("print", postTitle)
        postDescription = request.POST['postDescription']
        print(request.user.id)
        posted_user = User.objects.get(id=request.user.id)
        PostData.user = posted_user
        PostData.postDescription = postDescription
        PostData.postTitle = postTitle
        posts_user.save()
        print("date saved")
        print("1234567890",posted_user.id)
        # PostData(postTitle,postDescription,posted_user).save()
    return render(request,'registration/posts.html')