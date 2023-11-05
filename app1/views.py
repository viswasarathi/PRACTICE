from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def index(request):
    # temp = Student.objects.all().values()
    # out = ""
    # for x in temp:
    #     out += x['firstname'] + " " + x['lastname']
    # return HttpResponse(out)
    return render(request,'index.html')


def add(request):
    x = request.POST["first"]
    y = request.POST["last"]
    
    temp = Student(firstname = x ,lastname = y)
    temp.save()
    data = Student.objects.all().values()
    return render(request,'add.html',{'temp1':data})


