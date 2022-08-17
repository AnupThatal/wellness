from cProfile import Profile
from cgitb import text
from email import message
import email
from pyexpat.errors import messages
import re
from timeit import default_timer
from unicodedata import category, name
from urllib import request
from django.shortcuts import redirect, render
from django.test import RequestFactory
from pip import main
from .models import course,email_subscription,trainer,blog,profile
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import NewUserForm,blogForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView




def home(request):
    if request.method=="POST":
        Name=request.POST['Name']
        Email=request.POST['Email']
        Phone=request.POST['Phone']
        classes=request.POST['classes']
        message=request.POST['messages']
        recipent_list=[Email]

        email_from = settings.EMAIL_HOST_USER

        text='Name:'+ str(Name)  + '\n' + 'Email:' + str(Email) +'\n'+ 'Phone:' + str(Phone) +'\n'+ 'classes:' + str(classes)+'\n' + 'message:' +str(message) 

        
        message = EmailMessage("New request for course",text,email_from,recipent_list)
        message.send()

        return redirect('/')
    else:
        teacher=trainer.objects.all()
        courses=course.objects.all()

        return render(request,'index.html',{'trainer':teacher,'course':courses})

def courses(request):
    courses=course.objects.all()
    
    return render(request,'classes.html',{'course':courses})

def course_detail(request,pk):

    course_details=course.objects.get(pk=pk)
    return render(request,'classes-details.html',{'course':course_details})

def blogs(request):
    
    b=blog.objects.all()

    latest_blog=blog.objects.all()[:1]

    return render(request,'blog.html',{'blog':b,'latest':latest_blog})

    # return render(request,'blog.html')

def blog_detail(request,pk):

    blog_details=blog.objects.get(pk=pk)

    
    return render(request,'blog-details.html',{'blog':blog_details})

# def register(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             nation=form.cleaned_data['nationality']
#             f=form.cleaned_data['firstname']
#             l=form.cleaned_data['lastname']
#             e= form.cleaned_data['email']
          


#             profile.objects.create(user=user,nationality=nation,firstname=f,lastname=l,email=e)



          
#             return redirect('login')
#     else:
#         form = NewUserForm()
#     return render(request,'register.html',{'form':form})

# def login(request):
#     if request.method == 'POST':
   
#         # AuthenticationForm_can_also_be_used__
   
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user is not None:
#             form = auth_login(request, user)
#             messages.success(request, f' wecome {username} !!')
#             return redirect('/')
#         else:
#             messages.info(request, f'account done not exit plz sign in')
#     form = AuthenticationForm()
#     return render(request, 'login.html', {'form':form, 'title':'log in'})

# def logout(request):
# 	auth_logout(request)
# 	messages.info(request, "You have successfully logged out.")
#     # print("hey you have been logout") 
# 	return redirect("/")


def about(request):
    latest_blog=blog.objects.all()[:1]


    return render(request,'about-us.html',{'latest':latest_blog})


# @login_required
# def profiles(request):
#     user_details=profile.objects.filter(user=request.user)
#     return render(request,'profile.html',{'user':user_details})


def email(request):
    if request.method == "POST":

        email2=request.POST.get('email')
        email_subscription.objects.create(email=email2)
        redirect('/')

    
    return render(request,'index.html')

# def course_filter(request):
#     return render(request,'classes.html')


        
# @login_required
# def blog_create(request):
#     if request.method == 'POST':
#         form = blogForm(request.POST,request.FILES)
#         if form.is_valid():
#             post=form.save(commit=False)
#             post.username=request.user
#             # title=form.cleaned_data['title']
#             # top_content=form.cleaned_data['top_content']
#             # content=form.cleaned_data['content']
#             # main_pic1=form.cleaned_data['main_pic1']
#             # pic1=form.cleaned_data['pic1']
#             # pic2=form.cleaned_data['pic2']
#             # Date=form.cleaned_data['Date']
#             # category=form.cleaned_data['category']
#             # important_notes=form.cleaned_data['important_notes']
#             # username = request.user
#             # post = blog.objects.create(title = title,top_content=top_content,content = content,important_notes=important_notes,main_pic1 =main_pic1,pic1=pic1,pic2=pic2,username=username,category=category)
#             form.save()
#             return redirect('blogs')
#     else:
#         form = blogForm()
#     return render(request,'create-blog.html', {"form": form})

# @login_required
# def delete_post(request,pk):
#     post_to_delete=blog.objects.get(pk=pk)
#     post_to_delete.delete()
#     return redirect('/')
    
# def update_post(request,pk):
#     post=blog.objects.get(pk=pk)
#     form=blogForm(request.POST or None,instance=post)

#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     return render(request,'create-blog.html',{'form':form,'post':post})

# def payment(request):
#     return render('')
