from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from .models import User, Complaint, Fir
from django.views.generic import CreateView, UpdateView, FormView, DetailView, View, ListView
from .forms import RegisterForm, ComplainForm, Statusform, FirForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# def index(request):
#     return render(request, 'index.html',)
from .serializers import ComplaintSerializer


class index(LoginRequiredMixin, View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        user_object = User.objects.get(pk=request.user.id)
        return render(request, self.template_name, {'object': user_object})


class dashboard(View):
    template_name = 'mycomplaint.html'
    def get(self, request, *args, **kwargs):
        user_object = User.objects.get(pk=request.user.id)
        return render(request, self.template_name, {'object': user_object})

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        print(username)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('<h2> Account Not Active </h2>')

        else:
            print('Someone tried to login failed on our site.')
            return HttpResponse('<h2>Invalid login credentials applied </h2>')

    else:
        return render(request, 'login_view.html', {})


class register(FormView):
    form_class = RegisterForm
    template_name = 'registration.html'
    print("hello")
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('login_view'))

class AccountSettings(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'location', 'phone_no', 'profile_image','id_num','id_pic']
    template_name = 'user_profileupdate.html'
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Your Account Settings were updated successfully!')
        return reverse('index')

'''
Complaint view
'''

class RegisterComplaint(SuccessMessageMixin, CreateView):
    form_class = ComplainForm
    template_name = 'complaintform.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.seen_by = None
        form.save()

        messages.success(self.request,
                         'Your complaint was registered successfully, one of our correspondents would soon get back to you')

        return HttpResponseRedirect(reverse('index'))

class ListComplaints(ListView):
    model = Complaint
    template_name = 'ListComplaints.html'



class DetailComplaints(DetailView, CreateView):
    form_class = Statusform
    model = Complaint
    template_name = 'DetailComplaints.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        # form.instance.seen_by = None
        form.save()
        return HttpResponseRedirect(reverse('ListComplaints'))

    def update_seen_by(self):
        self.object.seen_by = self.request.user
        print(str(self.object))

class mycomplaintlist(ListView):
    model = Complaint
    template_name = 'mycomplaintlist.html'

    def get(self, request,pk):
        user_object = Complaint.objects.get(created_by=request.user.id)
        return render(request, self.template_name, {'object': user_object})

class myfir(ListView):

    model = Fir
    template_name = 'myfir.html'

    def get(self, request,pk):
        user_object = Fir.objects.get(created_by=request.user.id)
        print(user_object)
        return render(request, self.template_name, {'object': user_object})

def viewlist(request):
    datas = reversed(User.objects.all())
    return render(request, 'viewusers.html',{'datas': datas})



def deleteuser(request,dataid):
    if request.user.is_superuser:
        User.objects.filter(id=dataid).delete()
    return redirect('viewlist')



class ComplaintView(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = (permissions.AllowAny)
    def post(self, request, format=None):
        return Response("ok")

    def get_queryset(self):
        user = self.request.user
        return Complaint.objects.filter(created_by=user)


class ComplaintList(generics.ListAPIView):
    serializer_class = ComplaintSerializer
    def get_queryset(self):
        user = self.request.user
        return Complaint.objects.filter(created_by=user)

def fir_create(request,pk):
    # complaintid = get_object_or_404(Complaint,id=pk)
    instance2 = Complaint.objects.filter(id=pk)
    form = FirForm(request.POST or None)
    if form.is_valid():
        instance2.status = "FIR Filed"
        instance2.save()
        messages.success(request,"FIR filed successfully")
        return HttpResponseRedirect('mycomplaintlist')
    context={
    "form":form,
    }
    return render(request,"fir_form.html",context)

class myfir(ListView):
    model = Fir
    template_name = 'myfir.html'
    def get(self, request,pk):
        user_object = Fir.objects.get(created_by=request.user.id)
        return render(request, self.template_name, {'object': user_object})