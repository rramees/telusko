from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):

    prod1 = Product()
    prod1.prod_name = 'Iphone'
    prod1.desc = 'All new Iphone 15 pro Max'
    prod1.image = 'app-1.jpg'

    prod2 = Product()
    prod2.prod_name = 'Apple Watch'
    prod2.desc = 'All new Apple Watch'
    prod2.image = 'product-1.jpg'

    prod3 = Product()
    prod3.prod_name = 'Face cream pack'
    prod3.desc = 'Clear your pimples with the all new face cream pack'
    prod3.image = 'branding-1.jpg'

    products = [prod1 , prod2 , prod3 ]
    
    return render(request, 'index.html' ,{'products': products})



def hospital_management_system(request):
    return render(request, 'hospital_management_system.html')

def order_tracking_solution(request):
    return render(request, 'order-tracking-solution.html')

def track_and_trace(request):
    return render(request, 'track-and-trace.html')

def materiflow_pro(request):
    return render(request, 'materiflow-pro.html')
