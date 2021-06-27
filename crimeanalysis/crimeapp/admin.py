from django.contrib import admin
from . models import User, Complaint,Fir

# Register your models here.
admin.site.register(User)
admin.site.register(Complaint)
admin.site.register(Fir)