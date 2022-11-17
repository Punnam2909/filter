from django.shortcuts import render
from .models import addof

# Create your views here.

def add(request):
    if request.method == "POST":
        name = request.POST['name']
        print(name)
        data = addof(name=name)
        data.save()
    return render(request,'update/add.html',{})

