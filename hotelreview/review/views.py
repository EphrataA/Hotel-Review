from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Contact, Rate

# Create your views here.


def home(request):
   
   return render(request, 'review/home.html', {})

def about(request):
   
   return render(request, 'review/about.html')

def blog(request):
  
   return render(request, 'review/blog.html')

def categories(request):
   
   return render(request,'review/categories.html')

def page(request):
   if request.method == "GET":
      rate = request.GET.get('rate')
      comment = request.GET.get('comment')

   return render(request,'review/page.html')

def contact(request):
   if request.method == "POST":
 
      name = request.POST.get('name')
      email = request.POST.get('email')
      message = request.POST.get('message')
   
      contact = Contact()
      print("######################################")
      print(contact)
      contact.name = name
      contact.email = email
      contact.message = message
      contact.save()
      print(contact)
      
      
      print("######################################")

   return render(request,'review/contact.html')
