from http.client import HTTPResponse
from urllib import response
from django.shortcuts import HttpResponse, render
from home.models import Form

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is home page")

def form(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        description = request.POST.get('description')
        form = Form(fname=fname, lname=lname, email=email, description=description )
        form.save()
        #response.set_cookie('cfname', fname)
        #response.set_cookie('clname', lname)
        #response.set_cookie('status', True)
    return render(request, 'form.html')
    #return HttpResponse("this is form page")