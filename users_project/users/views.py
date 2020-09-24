from django.shortcuts import render, HttpResponse, redirect
from .models import Users
# Create your views here.

def index(request):
    context = {
        "all_users" : Users.objects.all(), 
    }
    return render(request, "index.html", context)

def addUser(request):
    # print(dict(request.POST))
    newFirst = request.POST['new_first']
    newLast = request.POST['new_last']
    newEmail = request.POST['new_email']
    newAge = request.POST['new_age']
    Users.objects.create(first_name = newFirst, last_name=newLast, email_address=newEmail, age=newAge)
    return redirect("/")