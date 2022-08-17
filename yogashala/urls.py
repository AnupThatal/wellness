from atexit import register
from re import template
from unicodedata import name
from venv import create
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from yogashala.models import course, profile
from .views import blog_detail, course_detail,courses, email,home,blogs,about


urlpatterns = [
    path('',home,name='home'),
    path('courses',courses,name='courses'),
    path('course-detail/<int:pk>',course_detail,name='course_detail'),
    path('blog',blogs,name='blogs'),
    path('blog-detail/<int:pk>',blog_detail,name='blog_detail'),
    # path('register/',register,name='register'),
    # path('login/',login,name='login'),
    # path('logout/',logout,name='logout'),
    # path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name='reset_password'),
    # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    # path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),
    path('about/',about,name='about'),
    # path('profiles/',profiles,name='profiles'),
    path('email/',email,name='email'),
    # path('course-filter/',course_filter,name='course_filter'),
    # path('blog-create',blog_create, name='blog_create'),
    # path('blog-delete/<int:pk>',delete_post,name='delete_post'),
    # path('blog-update/<int:pk>',update_post,name='update_post')
    


]

