from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html' ,{'name':'Ramees'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    sum = val1 + val2
    return render(request, 'result.html' ,{'result':sum,'number1':val1, 'number2':val2})    