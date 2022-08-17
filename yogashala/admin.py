from django.contrib import admin

from yogashala.views import email_subscription
from .models import course,trainer,blog,category,profile
# Register your models here.

admin.site.register(trainer)
admin.site.register(course)
admin.site.register(blog)
admin.site.register(category)
admin.site.register(profile)
admin.site.register(email_subscription)