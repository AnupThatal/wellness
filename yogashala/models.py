from copyreg import pickle
from pyexpat import model
from sqlite3 import Date
from statistics import mode
from turtle import back
from unicodedata import category
from xmlrpc.client import DateTime
from django.db import models
import uuid  # Import the UUID module
import os
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class course(models.Model):
    id = models.AutoField(primary_key=True)  # Create an AutoField primary key
    course_name=models.CharField(max_length=1000,unique=False,null=False,blank=False)
    file_mainpic=models.FileField(unique=False,blank=False)
    trainer_name=models.ForeignKey('Trainer',on_delete=models.CASCADE,related_name='trainers_profile')
    title=models.TextField(max_length=200,null=False,blank=False)
    Description=models.TextField(null=False,blank=False)
    quotes=models.TextField(null=False,blank=False)
    important_notes=models.TextField(null=False,blank=False)
    price=models.IntegerField(null=False,blank=False)
    pic1=models.FileField(null=False,blank=False)
    pic2=models.FileField(blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    offers=models.CharField(max_length=500,blank=True,null=True,default='0')
    # offers_date= models.DateField(default=timezone.now, blank=True, null=True)
    offers_date = models.DateField(blank=True, null=True)
    subject_email=models.CharField(blank=True, null=True)
    def __str__(self):
        return self.course_name

    def filename(self):
        return os.path.basename(self.file_mainpic.name)
    

COUNTRY_CHOICES = [
        ('India', 'India'),
        ('Nepal', 'Nepal'),
        ('Canada', 'Canada'),
        ('USA', 'USA'),
        ('Australia', 'Australia'),
    ]   

class Trainer(models.Model):
    id = models.AutoField(primary_key=True)  # Create an AutoField primary key

    trainer_name=models.CharField(max_length=150,null=False,blank=False)
    expertise=models.CharField(max_length=1000,null=False,blank=False)
    trainer_pic=models.FileField(null=False,blank=False)
    country = models.CharField(max_length=100,null=False,blank=False)
    city=models.CharField(max_length=300,null=False,blank=False)
    location=models.CharField(max_length=300,null=False,blank=False)
    contact=models.CharField(max_length=20,null=False,blank=False)
    desc = models.TextField(null=True, blank=True)

    Email=models.EmailField(max_length=150,null=False,blank=False)
    
    is_trainer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.trainer_name



class course_buy(models.Model):
    id = models.AutoField(primary_key=True)  # Create an AutoField primary key
    name = models.CharField(max_length=100,null=False,blank=False)
    country = models.CharField(max_length=100,null=False,blank=False)
    puja_date = models.DateField(null=False,blank=False)
    Email = models.EmailField(null=False,blank=False)
    contact = models.CharField(null=False,blank=False)
    payment = models.CharField(null=False,blank=False)
    address = models.TextField(max_length=500,null=False,blank=False)
    puja_name= models.ForeignKey(course, on_delete=models.CASCADE)
    message=models.TextField(default='')
    paid=models.BooleanField(default=False,choices=[
            (True, 'Yes'),
            (False, 'No')
        ])
    completed=models.BooleanField(default=False,choices=[
            (True, 'Yes'),
            (False, 'No')])
    
class category(models.Model):
    category=models.CharField(max_length=1000)

    def __str__(self):
        return self.category


class blog(models.Model):
    title=models.CharField(max_length=1000,null=False,blank=False)
    top_content=models.TextField(null=False,blank=False)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(null=False,blank=False)
    important_notes=models.TextField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    main_pic1=models.FileField(null=False,blank=False)
    pic1=models.FileField(null=False,blank=False)
    pic2=models.FileField(null=False,blank=False)
    Date=models.DateField(null=False,blank=True)

     
    def __str__(self):
        return self.title

class Itemcart(models.Model):
    id = models.AutoField(primary_key=True)  # Create an AutoField primary key
    items = models.ManyToManyField(course, related_name='course')
    purchase_date = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_purchased = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    name=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=50, null=True, blank=True)
    quantity= models.CharField(max_length=20, null=True, blank=True)
    Any_sepcial_request = models.TextField(null=True, blank=True)

    def __str__(self):
        course_names = ', '.join([str(course) for course in self.items.all()])
        return f"Purchased Courses: {course_names}"




class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nationality=models.CharField(max_length=200,blank=False)
    email = models.EmailField(blank=False,)
    firstname=models.CharField(blank=False,max_length=200)
    lastname=models.CharField(blank=False,max_length=300)
    

    def __str__(self):
        return self.firstname

class email_subscription(models.Model):
    email=models.EmailField(unique=True)


    def __str__(self):
        return self.email


@receiver(post_save,sender=course)
def send_blog_notification(sender,instance,created,**kwargs):
    if created:
        subscribers=email_subscription.objects.all()
        
        email_from = settings.EMAIL_HOST_USER
        
        subject = instance.subject_email

        for subscriber in subscribers:
            recipient_email=subscriber.email
                
            if instance.offers=='0' and instance.subject_email is not None:
                context = {
                'name':instance.course_name,
                'Description':instance.Description,
                # 'Date':instance.offers_date,

                }
                html_version = 'email.html'
                html_message = render_to_string(html_version, {'context': context})
                message = EmailMessage(subject,html_message,email_from,[recipient_email])
                message.content_subtype = 'html'
                message.send()
                
            # else:
            #     context = {
            #  'name':instance.course_name,
            #  'Description':instance.Description,
            #  'offers':instance.offers
             
            #  }
            #     html_version = 'email.html'
            #     html_message = render_to_string(html_version, {'context': context})
            #     message = EmailMessage(subject,html_message,email_from,[recipient_email])
            #     message.content_subtype = 'html'
            #     message.send()
    if not created:
        subscribers=email_subscription.objects.all()
        email_from = settings.EMAIL_HOST_USER
        subject = instance.subject_email
        for subscriber in subscribers:
            recipient_email=subscriber.email
            if instance.offers!='0' and instance.offers_date is not None and instance.subject_email:
                context = {
                        'name':instance.course_name,
                        'Description':instance.Description,
                        'offers':instance.offers,
                         'date':instance.offers_date             
                    }
                html_version = 'email.html'
                html_message = render_to_string(html_version, {'context': context})
                message = EmailMessage(subject,html_message,email_from,[recipient_email])
                message.content_subtype = 'html'
                message.send()
                
                # else:
                #     context = {
                #     'name':instance.course_name,
                #     'Description':instance.Description,
                #     'offers':instance.offers
                #     }
                #     html_version = 'email.html'
                #     html_message = render_to_string(html_version, {'context': context})
                #     message = EmailMessage(subject,html_message,email_from,[recipient_email])
                #     message.content_subtype = 'html'
                #     message.send()
    



    



