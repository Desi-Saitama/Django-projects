from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    
    people = [
        {'name':'Dev', 'age':20},
        {'name':'Atul','age':21},
        {'name':'Sani','age':22},
        {'name':'Sarthak','age':30},
        {'name':'Parth','age':24},
    ]

    return render(request, "index.html", context={'people':people})

def sucess_page(request):
    return HttpResponse("<h1>This is a success</h1>")