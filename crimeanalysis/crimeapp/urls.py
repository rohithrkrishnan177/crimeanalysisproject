from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('crimeanalysis', views.ComplaintView)
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.login_view, name='login_view'),
    # path('dashboard', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login_view.html'), name='logout'),
    path('register', views.register.as_view(), name='register'),
    path('settings/<int:pk>', views.AccountSettings.as_view(), name='settings'),
    path('index/', views.index.as_view(), name='index'),
    path('settings/<int:pk>', views.AccountSettings.as_view(), name='settings'),
    # Change Password
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name='change_password.html',success_url = '/'),name='change_password'),
    path('viewlist', views.viewlist, name='viewlist'),
    path('mycomplaintlist/<int:pk>', views.mycomplaintlist.as_view(), name='mycomplaintlist'),


    # Complaint
    path('my_complaints/', views.ComplaintList.as_view(), name='my_complaints'),
    path('api/', include(router.urls)),
    path('complaintform/', views.RegisterComplaint.as_view(), name='complaintform'),
    path('ListComplaints/', views.ListComplaints.as_view(), name='ListComplaints'),
    path('DetailComplaints/<int:pk>', views.DetailComplaints.as_view(), name='DetailComplaints'),
    path('mycomplaint/', views.dashboard.as_view(), name='mycomplaint'),
    path('deleteuser/<int:dataid>', views.deleteuser, name='deleteuser'),
    path('fir_create/<int:pk>', views.fir_create, name='fir_create'),
    path('myfir/<int:pk>', views.myfir.as_view(), name='myfir'),

]