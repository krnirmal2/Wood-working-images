from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# here we import the models contents to the admin panel that are the category and the image clasee
# this admin.py is help to show all the contents in the admin panel

# Register your models here.   and after that we can login to our admin panel
admin.site.register(Category)
admin.site.register(Image)
