from django.shortcuts import render

# Create your views here.
def script(request):
    return render(request,'index.html')