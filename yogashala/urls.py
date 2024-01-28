from atexit import register
from re import template
from unicodedata import name
from venv import create
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from yogashala.models import course, profile
from .views import blog_detail, course_detail, course_purchase,courses, email,home,blogs,about,esewapayment,course_purchase,booked,add_cart,findpandit,view_cart,remove_from_cart,create_pandit,course_purchase_cart


urlpatterns = [
    path('',home,name='home'),
    path('courses',courses,name='courses'),
    path('course-detail/<int:pk>',course_detail,name='course_detail'),
    path('blog',blogs,name='blogs'),
    path('blog-detail/<int:pk>',blog_detail,name='blog_detail'),
    path('about/',about,name='about'),
    path('email/',email,name='email'),
    path('esewapayment/',esewapayment,name='esewapayment'),
    path('course_purchase/<int:pk>',course_purchase,name='course_purchase'),
    path('add_cart/<int:pk>',add_cart,name='add_cart'),
    path('course_purchase_cart/',course_purchase_cart, name='course_purchase_cart'),
    path('booked/',booked,name='booked'),
    path('findpandit/<str:name>/',findpandit, name='findpandit'),
    path('view_cart/',view_cart,name='view_cart'),    
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('create_pandit/',create_pandit,name='create_pandit'),    
]

