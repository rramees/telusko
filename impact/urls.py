from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name= 'index'),
    path('hospital-management-system/', views.hospital_management_system, name='hospital_management_system'),
    path('order-tracking-solution/', views.order_tracking_solution, name='order_tracking_solution'),
    path('track-and-trace/', views.track_and_trace, name='order_tracking_solution'),
    path('materiflow-pro/', views.materiflow_pro, name='materiflow_pro'),

    





]