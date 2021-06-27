from django.contrib.auth.forms import UserCreationForm
from .models import User, complaintstat, Complaint, Fir
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'location', 'phone_no', 'profile_image','id_num','id_pic']


class ComplainForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ['created_by','title', 'category', 'description', 'location', 'evidence']


class Statusform(forms.ModelForm):

    class Meta:
        model = complaintstat
        fields = ['created_by','title','action', 'assigned']

class FirForm(forms.ModelForm):
    class Meta:
        model = Fir
        fields = ["firid", "signedby", "content"]