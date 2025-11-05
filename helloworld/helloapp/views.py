from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request,'home.html',{'name':"python"})
# Create your views here.
def add(request):
    #val_1=int(request.GET['num_1'])
    #val_2=int(request.GET['num_2'])
    val_1=int(request.POST['num_1'])
    val_2=int(request.POST['num_2'])
    res=val_1+val_2

    return render(request,'result.html',{'result':res})