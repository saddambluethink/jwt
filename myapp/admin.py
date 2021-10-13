from django.contrib import admin
# import moadel here than register
from .models import employee

# Register your models here.
admin.site.register(employee)


# run the commond = python manage.py makemigrations
# python manage.py migrate 
# python manage.py createsuperuser
