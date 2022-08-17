from copyreg import pickle
from pyexpat import model
from sqlite3 import Date
from statistics import mode
from turtle import back
from unicodedata import category
from xmlrpc.client import DateTime
from django.db import models
import os
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.template.loader import render_to_string
# from email.message import EmailMessage
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.models import AbstractUser
# from django_countries.fields import CountryField
from django_countries.fields import CountryField
from flask import request    

# Create your models here.





class course(models.Model):
    course_name=models.CharField(max_length=1000,unique=False,null=False,blank=False)
    file_mainpic=models.FileField(unique=False,blank=False)
    trainer_name=models.ForeignKey('trainer',on_delete=models.CASCADE,related_name='trainers_profile')
    Description=models.TextField(null=False,blank=False)
    price=models.IntegerField(null=False,blank=False)
    week=models.CharField(null=False,blank=False,max_length=150)    
    pic1=models.FileField(null=False,blank=False)
    Date=models.TimeField(null=False,blank=False)
    location=models.CharField(null=False,blank=False,max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name
    
    def filename(self):
        return os.path.basename(self.file_mainpic.name)

class trainer(models.Model):
    trainer_name=models.CharField(max_length=150,null=False,blank=False)
    expertise=models.CharField(max_length=1000,null=False,blank=False)
    trainer_pic=models.FileField(null=False,blank=False)
    def __str__(self):
        return self.trainer_name




@receiver(post_save, sender=course)
def send_tracking_email(sender, instance,**kwargs):
    subject = 'yog school'
    email_from = settings.EMAIL_HOST_USER
    recipent_list=[instance.user.email]
    print(recipent_list)
    context={
        'course_name':instance.course_name,
        'Description':instance.Description,
        'trainer_name':instance.trainer_name,
        'Date':instance.Date
    }

    html_version ='email.html'
    html_message = render_to_string(html_version,{'context':context})
    message = EmailMessage(subject,html_message,email_from,recipent_list)
    message.content_subtype = 'html' # this is required because there is no plain text email version
    message.send()


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

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nationality=models.CharField(max_length=200,blank=False)
    email = models.EmailField(blank=False,)
    firstname=models.CharField(blank=False,max_length=200)
    lastname=models.CharField(blank=False,max_length=300)
    

    def __str__(self):
        return self.firstname

# @receiver(post_save,sender=User)
# def create_user(sender,updated,created,instance,**kwargs):
#     if created or updated:
#         profile.objects.update_or_create(Username=instance.user,nationality=instance.nationality,firstname=instance.f,lastname=instance.l,email=instance.e)

class email_subscription(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email


# class comments(models.Model):
#     comment=models.CharField(max_length=100000)
#     blog=models.ForeignKey(blog,on_delete=models.CASCADE)




