
import re
from unicodedata import category
from django.shortcuts import render
from numpy import product
from .forms import UserReg,ProdReg
from .models import Product, User

# Create your views here.
def add(request):
    if request.method =='POST':
        fm = UserReg(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = UserReg()
    
    return render(request,'myapp/add.html',{'form':fm})




def show(request):
    stud = User.objects.all()
    return render(request,'myapp/show.html',{'stud':stud})
    



# For updating purpose

def update_data(request,id):
    if request.method == 'POST':
        elem = User.objects.get(pk=id)
        fm = UserReg(request.POST,instance=elem)
        if fm.is_valid:
            fm.save()

    else:
        elem = User.objects.get(pk=id)
        fm = UserReg(instance=elem)

    return render(request,'myapp/update.html',{'form':fm})



# ------------------------------------------------------------------------------


# For products

def addp(request):
    if request.method =='POST':
        fm = ProdReg(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = ProdReg()
    
    return render(request,'myapp/addp.html',{'form':fm})




def showp(request):
    prod = Product.objects.all()
    return render(request,'myapp/showp.html',{'prod':prod})
    




def update_datap(request,id):
    if request.method == 'POST':
        elem = Product.objects.get(pk=id)
        fm = ProdReg(request.POST,instance=elem)
        if fm.is_valid:
            fm.save()

    else:
        elem = Product.objects.get(pk=id)
        fm = ProdReg(instance=elem)

    return render(request,'myapp/updatep.html',{'form':fm})


def details(request,id):
    elem = Product.objects.get(pk=id)
    return render(request,'myapp/details.html',{'elem':elem })


def recommendation(request,id):
    elem = Product.objects.get(pk=id)
    rel_prod = Product.objects.filter(shape=elem.shape).exclude(pk=id)
    return render(request,'myapp/recommendation.html',{'related':rel_prod})
