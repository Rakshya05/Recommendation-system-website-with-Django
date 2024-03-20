from django.contrib import admin

from app1.models import CustomUser
from contactapp.models import contacts

# Register your models here.
admin.site.register(contacts)
