from cProfile import Profile
from collections import Counter
from cgitb import text
from email import message
from django import forms
import email
from datetime import date  # Import the date module
from pyexpat.errors import messages
import pandas as pd
import re
from timeit import default_timer
from unicodedata import category, name
from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from django.test import RequestFactory
from pip import main
from .models import course,email_subscription,blog,course_buy,profile,Itemcart,Trainer
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
from .forms import NewUserForm,blogForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.template.loader import render_to_string  # Import render_to_string
from datetime import datetime

def home(request):
    if request.method=="POST":
        Name=request.POST['Name']
        Email=request.POST['Email']
        Phone=request.POST['Phone']
        classes=request.POST['classes']
        message=request.POST['messages']
        recipient_email=[Email]
        email_from = settings.EMAIL_HOST_USER
        subject = 'New Appointment'
        recipient_email=str(recipient_email[0])
        print(recipient_email)
        context = {
        'course_name': Name,
        'Description': message,
        'classes': classes,
        }

        html_version = 'email.html'
        html_message = render_to_string(html_version, {'context': context})

        message = EmailMessage(subject,html_message,email_from,[recipient_email])
        message.content_subtype = 'html'
        
        try:
            message.send()
            return redirect('/')  
        except Exception as e:
            return HttpResponse("Error: " + str(e))  


    else:
        b=blog.objects.all()
        teacher=Trainer.objects.all()
        courses=course.objects.all()
        latest_blog=blog.objects.order_by('Date')[:3]
        cart = request.session.get('cart', [])
        cart_count = len(cart)
        return render(request,'index.html',{'trainer':teacher,'course':courses,'latest_b':latest_blog,'count':cart_count})
    
def courses(request):
    courses=course.objects.all()
    teacher=Trainer.objects.all()
    cart = request.session.get('cart', [])
    cart_count = len(cart)
    return render(request,'classes.html',{'course':courses,'trainer':teacher,'count':cart_count})

def course_detail(request,pk):
    courses=course.objects.all()[:3]
    course_details=course.objects.get(pk=pk)
    teacher=Trainer.objects.all()
    cart = request.session.get('cart', [])
    cart_count = len(cart)
    return render(request,'classes-details.html',{'course':course_details,'c':courses,'trainer':teacher,'count':cart_count})


def add_cart(request, pk):
    product = get_object_or_404(course, pk=pk)
    cart = request.session.get('cart', [])
    cart.append({'id':product.id,'name': product.course_name, 'price': float(product.price),'title':product.title,'img':product.file_mainpic.url,'quantity':1})
    request.session['cart'] = cart
    return redirect('courses')

def view_cart(request):
    cart = request.session.get('cart',[])
    if cart:
        df=pd.DataFrame(cart)
        df1=df.value_counts().reset_index()
        print(df1)
        df1['price']=df1['price']*df1['count']
        cart= df1.to_dict(orient='records')
        total_price = sum(item['price'] for item in cart)   
        
        return render(request,'cart.html', {'carts':cart, 'total_price': total_price})
    else:
        empty_cart_message = "Your cart is empty. Please add items before proceeding to book."
        return render(request, 'cart.html', {'carts': [], 'total_price': 0, 'empty_cart_message': empty_cart_message})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart',[])
    cart = [item for item in cart if item['id'] != product_id]
    # print(cart)
    request.session['cart'] = cart    
    return redirect('view_cart')  # Redirect to the cart view


def blogs(request):
    b=blog.objects.all()
    latest_blog=blog.objects.order_by('Date')[:3]
    teacher=Trainer.objects.all()
    cart1 = request.session.get('cart',[])
    cart_count=len(cart1)

    return render(request,'blog.html',{'blog':b,'latest':latest_blog,'trainer':teacher,'count':cart_count})

def blog_detail(request,pk):
    blog_details=blog.objects.get(pk=pk)
    latest_blog=blog.objects.order_by('Date')[:3]
    teacher=Trainer.objects.all()
    cart1 = request.session.get('cart',[])
    cart_count=len(cart1)

    return render(request,'blog-details.html',{'blog':blog_details,'latest_b':latest_blog,'trainer':teacher,'count':cart_count})


def about(request):
    latest_blog=blog.objects.all()[:1]
    teacher=Trainer.objects.all()
    cart1 = request.session.get('cart',[])
    cart_count=len(cart1)
    return render(request,'about-us.html',{'latest':latest_blog,'trainer':teacher,'count':cart_count})


def email(request):
    if request.method == "POST":
        email2=request.POST.get('email')
        email_subscription.objects.create(email=email2)
        redirect('/') 
    return render(request,'index.html')

def booked(request):
    c=course.objects.all()[:3]
    teacher=Trainer.objects.all()
    cart1 = request.session.get('cart',[])

    cart_count=len(cart1)
    return render(request,'booked.html',{"course":c,'trainer':teacher,'count':cart_count})


def esewapayment(request):
    teacher=Trainer.objects.all()
    return render(request,'esewapayment.html',{'trainer':teacher})

def course_purchase(request,pk):
    course_details = course.objects.get(pk=pk)
    print(course_details)

   
    email_sub=email_subscription.objects.all()
    if request.method=="POST":
        
        Name1 = request.POST['firstname']
        country1 = request.POST['country']
        puja_date1 = request.POST['puja_date']
        email1 = request.POST['email']
        Phone1 = request.POST['phone_number']
        payment1 = request.POST['payment']
        address1 = request.POST['address']
        

        puja_date_obj = date.fromisoformat(puja_date1)


        print("Name1:", Name1)
        print("Country1:", country1)
        print("Puja Date1:",puja_date_obj)
        print("Email1:", email1)
        print("Phone1:", Phone1)
        print("Payment1:", payment1)
        print("Address1:", address1)
       

        print(type(course_details.course_name))
        cart1 = request.session.get('cart',[])
        cart_count=len(cart1)



        if payment1=='esewa':
            total=int(course_details.price)
            return render(request,'esewapayment.html',{'course':course_details,'t':total})
        elif payment1=='cod':
            try:
                print(course_details.course_name)
                save_product=course_buy(name=str(Name1),country=str(country1),
                                            puja_name=course_details,
                                            puja_date=puja_date_obj,
                                            Email=email1,contact=str(Phone1),payment=str(payment1),
                                            address=str(address1),message='HEY How are you')
                print(str(save_product))
                print(save_product.save())

                email_sub = email_subscription.objects.filter(email=email1)

                if email_sub.exists():
                    pass
                else:
                    email_subscription.objects.create(email=email1)
                # message.success(request,'Booking has been please check your email')

                if save_product:
                     email_from = settings.EMAIL_HOST_USER
                     subject = 'Booking confirmation'
                     recipient_email=str(email1)
                     recipient_email1='anupthatal2@gmail.com'

                     context = {
                         'name':save_product.name,
                         'puja_date':course_details.course_name,
                         'country':save_product.country,
                        'address':save_product.address,
                        'payment':save_product.payment,
                        'puja_name':save_product.puja_name,
                        'price':course_details.price,
                        'id':save_product.id,
                        'date':save_product.puja_date
                        }
                     html_version = 'booking.html'
                     html_message = render_to_string(html_version, {'context': context})
                     message = EmailMessage(subject,html_message,email_from,[recipient_email,recipient_email1])
                     message.content_subtype = 'html'
                     try:
                         message.send()
                         return redirect('booked')  # Redirect to a success page
                     except Exception as e:
                         return HttpResponse("Error: " + str(e))  # Replace with your error handling logic
                    #  request.session['booking_successful'] = True
            except Exception as e:
                print(f"Error creating course_buy object: {e}")
    return render(request,'course_purchase.html',{'course':course_details})

def findpandit(request,name):
    print(str(name))
    teachers = Trainer.objects.filter(country=str(name), is_trainer=True)
    print("Number of teachers:", len(teachers))
    c = Trainer.objects.all()
    cart1 = request.session.get('cart',[])
    cart_count=len(cart1)
    return render(request,'find_pandit.html', {'c': c, 't': teachers, 'searched_name': name,'count':cart_count})

def create_pandit(request):
    if request.method == 'POST':
        t = request.POST.get('trainer_name')
        contact = request.POST.get('contact')
        country = request.POST.get('country')
        location = request.POST.get('location')
        city = request.POST.get('city')
        desc=request.POST.get('desc')
        email = request.POST.get('email')
        pic = request.FILES.get('pic') 
        print("t:", t)
        print("contact:", contact)
        print("country:", country)
        print("location:", location)
        print("city:", city)
        print("desc:", desc)
        print("email:", email)
        print("pic:", pic)



        print(country)


        t=Trainer(trainer_name=t,
                  country=country,
                  contact=contact,
                  expertise='Any Puja',location=location,trainer_pic=pic,
                  desc=desc,city=city,Email=email)
        t.save()        
        return redirect('/')
    else:
        # Handle GET request or other cases
        cart1 = request.session.get('cart',[])
        cart_count=len(cart1)
        return render(request,'create_pandit.html',{'count':cart_count})
def course_purchase_cart(request):
    cart = request.session.get('cart', [])
    df = pd.DataFrame(cart)
    df1 = df.value_counts().reset_index()
    df1['price'] = df1['price'] * df1['count']
    cart = df1.to_dict(orient='records')
    total_price = sum(item['price'] for item in cart)
    cart1 = request.session.get('cart',[])
    cart_count=len(cart1)

    if request.method == "POST":
        name = request.POST['name']
        country = request.POST['country']
        location = request.POST['location']
        email = request.POST['email']
        contact = request.POST['contact']
        payment = request.POST['payment_option']
        any_special_request = request.POST['any_special_request']

        if payment == 'esewa':
            total = int(total_price)
            return render(request, 'esewapayment.html', {'t': total})
        elif payment == 'cod':
            # Validate and create Itemcart instance here
            item_cart = Itemcart.objects.create(
                name=name,
                country=country,
                location=location,
                Email=email,
                contact=contact,
                Any_sepcial_request=any_special_request,
                total_price=total_price,
                
            )
            auto_generated_id = item_cart.id


            selected_course_names = [item['name'] for item in cart]
            courses = course.objects.filter(course_name__in=selected_course_names)

            # Set the many-to-many relationship
            item_cart.items.set(courses)

            course_names = [course.course_name for course in courses]


            # Construct email content
            context = {
                'name': name,
                'country': country,
                'address': location,
                'payment': payment,
                'puja_name': course_names,
                'price': total_price,
                'date': datetime.now().date(),
                'id': auto_generated_id
            }
            html_version = 'booking.html'
            html_message = render_to_string(html_version, {'context': context})

            # Send email
            email_from = settings.EMAIL_HOST_USER
            subject = 'Booking confirmation'
            recipient_email = str(email)
            recipient_email1 = 'anupthatal2@gmail.com'
            message = EmailMessage(subject, html_message, email_from, [recipient_email, recipient_email1])
            message.content_subtype = 'html'
            message.send()

            request.session['cart'] = []


            return redirect('booked')

    return render(request, 'course_purchase_cart.html', {'carts': cart, 'total_p': total_price,'cart':cart_count})