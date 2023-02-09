from django.shortcuts import render,redirect

# Create your views here.

def Login(request):
    return render(request,'login.html')
def Home(request):
    return render(request,'index.html')