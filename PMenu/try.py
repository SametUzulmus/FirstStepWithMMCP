from os import name
from django.shortcuts import render,redirect,HttpResponse
from .utils import get_demand, get_plot,demand_, get_supply,supply
import matplotlib.pyplot as plt
import numpy as np
from .SuppyDemand import ATuyg
def HomePage(request):
    return render(request,"Hpage/HomePage.html")

def Pmenu1(requests):
    return render(requests,"Hpage/_p_Menu1.html")

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
#######################################
def Pmenu2(request):

        return render(request,"Hpage/_p_Menu2.html")

def Pmenu2T(request):

    if request.method=="POST":
        if 'btn1' in request.POST:


            return render(request,"Hpage/_p_Menu2.html",{'Demand': Demand})
        if 'btn2' in request.POST:
        
        
            return render(request,"Hpage/_p_Menu2.html",{'Supply': Supply})
    


def Pmenu2A(request):

    if request.method=="POST":
        if 'btn2' in request.POST:
        
        
            return render(request,"Hpage/_p_Menu2.html",{'Supply': Supply})
        if 'btn1' in request.POST:
            return render(request,"Hpage/_p_Menu2.html",{'Demand': Demand})

    #else:
        #return render(request,"Hpage/_p_Menu2.html")
#############################################################3





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
        

#x=np.array([0,5,10])
    y=np.array([0,10,20])


    z=np.array([10,0])
    w=np.array([0,20])
    

    chart=get_plot(x,y,z,w)