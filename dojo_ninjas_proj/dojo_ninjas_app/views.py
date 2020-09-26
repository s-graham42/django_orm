from django.shortcuts import render, HttpResponse, redirect
from dojo_ninjas_app.models import *

# Create your views here.
def index(request):
    context = {
        "all_dojos" : Dojo.objects.all(),
    }
    return render(request, "index.html", context)

def add_a_dojo(request):
    Dojo.objects.create(name = request.POST['dojoName'], city = request.POST['dojoCity'], state = request.POST['dojoState'], desc = request.POST['dojoDesc'])
    return redirect("/")


def add_a_ninja(request):
    # print(f"selectDojo is: {request.POST['selectDojo']}")
    Ninja.objects.create(first_name = request.POST['firstName'], last_name = request.POST['lastName'], dojo = Dojo.objects.get(id = request.POST['selectDojo']))
    return redirect("/")

def delete_a_dojo(request):
    delete_this = Dojo.objects.get(id = request.POST['dojoDelete'])
    print(delete_this.name)
    delete_this.delete()
    return redirect("/")