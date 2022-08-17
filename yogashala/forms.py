from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField    
from django_countries import widgets, countries
from django_countries.widgets import CountrySelectWidget
from django.dispatch import receiver
from .models import profile,blog
from django.db.models.signals import post_save



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	nationality =forms.ChoiceField(widget=CountrySelectWidget,choices=countries)
	firstname=forms.CharField(required=True,max_length=200)
	lastname=forms.CharField(required=True,max_length=300)



	class Meta:
		model = User
		fields = ("username", "email",'firstname','lastname',"password1", "password2",'nationality')

class blogForm(forms.ModelForm):
	class Meta:
		model=blog
		fields='__all__'
		exclude=['username']