from django.shortcuts import render
from .models import Surname,Member
import datetime

# Create your views here.


def family(request):
    surnames=Surname.objects.all()
    members=Member.objects.all()
    context={
        "surnames": surnames,
        "members": members,
    }
    return render(request, "demo/family.html", context)


def selection(request, id):
    surnames = Surname.objects.get(id=id)
    members = Member.objects.filter(initial_name=surnames)
    context={
        "surnames": surnames,
        "members": members,
    }
    return render(request, "demo/selection.html", context)

# def add_data(request):
#     if request.method == "POST":
#         initial = request.POST['initial_name']
#         name = request.POST['person_name']
#         # dob = request.POST['person_dob']
#         print(name)
#         data = Member(initial_name=initial, person_name=name)
#         data.save()
#     return render(request,'demo/family.html')