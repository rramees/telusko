from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name= 'index'),
    path('hospital-management-system/', views.hospital_management_system, name='hospital_management_system'),


]