from os import name
from django.shortcuts import render,redirect,HttpResponse
from .utils import get_demand, get_plot,demand_, get_supply,supply,get_market
import matplotlib.pyplot as plt
import numpy as np
from .SuppyDemand import ATuyg
from .models import Book

P = (demand_.a + demand_.c) / (demand_.b + demand_.d)
Qd = (demand_.a - demand_.b * P)
Qs = -demand_.c + demand_.d * P
                                                    # Bunları globalde tanımla
price = np.linspace(0,demand_.a/demand_.b)
quantity_d = demand_.a - demand_.b*price
quantity_s = -supply.c + supply.d * price

yx = [0, Qd]
yy = [P,P]
dx = [Qd,Qd]
dy = [0,P]

Demand=get_demand(quantity_d,price,yx,yy,dx,dy)
Supply=get_supply(quantity_s,price,yx,yy,dx,dy)
Market=get_market(quantity_s,price,quantity_d,yx,yy,dx,dy)


def HomePage(request):
    return render(request,"Hpage/HomePage.html")

def Pmenu1(request):
    book=Book.objects.all()

    context = {                     # istediğimiz türde bilgiyi alıp,
        
        'book':book
        
    }
    return render(request,'Hpage/_p_Menu1.html',context)
    
    
    
 

def Pmenu2(request):

        if request.method=="POST":
            
            if 'btn1' in request.POST:
                return render(request,"Hpage/_p_Menu2.html",{'Demand': Demand})
            if 'btn2' in request.POST:
                return render(request,"Hpage/_p_Menu2.html",{'Supply': Supply})
            if 'btn3' in request.POST:
                return render(request,"Hpage/_p_Menu2.html",{'Market': Market})
        else:
            return render(request,"Hpage/_p_Menu2.html")

def Pmenu3(request):

    if request.method=="POST":

        a=request.POST["number1"]
        b=request.POST["number2"]
        a=int(a)
        b=int(b)
        
        context ={
            "Toplam":a+b
        }
        
        return render(request,'Hpage/_p_Menu3.html',context)
    else:
        return render(request,'Hpage/_p_Menu3.html')
        

