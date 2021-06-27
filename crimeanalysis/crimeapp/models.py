import uuid
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from . choices import CRIME_CATEGORY
# from Test import settings
from django.template.defaultfilters import slugify


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_pics', default='1.png')
    phone_no = models.CharField(max_length=10, default=00000)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    id_num = models.CharField(max_length=20, default=00000)
    id_pic = models.ImageField(upload_to='ids',)
    birth_date = models.DateField(null=True, blank=True)


    def get_absolute_url(self):
        return reverse('index')


CRIME_CATEGORY = (
    (1, ("Accident")),
    (2, ("Fraud")),
    (3, ("Robbery")),
    (4, ("Bullying")),
    (5, ("Cyber Crime")),
    (6, ("Other"))
)



class Complaint(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    category = models.IntegerField(choices=CRIME_CATEGORY, default=1)
    description = models.TextField(max_length=200)
    location = models.CharField(max_length=50)
    evidence = models.FileField(upload_to='evidence',default='1.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('allcomplaint')

    def __str__(self):
        return self.title


ACTION = (
    (1, ("Resistered")),
    (2, ("Received")),
    (3, ("Pending For Enquirey")),
    (4, ("Investigation")),
    (5, ("Action Taken")),
    (6, ("Closed"))
)
class complaintstat(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.ForeignKey(Complaint, on_delete=models.CASCADE, blank=True, null=True)
    action = models.IntegerField(choices=ACTION, default=1)
    statdate = models.DateTimeField(null=True, blank=True)
    assigned = models.CharField(max_length=50, blank=True, null=True)


class Fir(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Crime_No = models.UUIDField(default = uuid.uuid4,editable = False)
    firid=models.CharField(max_length=10,primary_key=True)
    signedby= models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    content=models.TextField(default="First Information Report not yet submitted")

    def  __unicode__(self):
        return self.firid

    def __str__(self):
        return self.firid