from django.shortcuts import redirect, render ,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def login(request):
    
    if request.method=="POST":

        username=request.POST["username"]
        password=request.POST["password"]
        
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.add_message(request,messages.SUCCESS,"Giriş Başarılı !")
            return redirect("HomePage")
        else:
            messages.add_message(request,messages.ERROR,"Kullanıcı Adı veya Parola Hatalı ! !")
            return redirect("login")
    else:
        
        return render(request,"user/login.html")
    
    
    
    
def register(request):

    if request.method=="POST":

        print("EVET POST")
        
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]

        if password==repassword:

            if User.objects.filter(username=username).exists():
                messages.add_message(request,messages.WARNING,"Bu Kullanıcı Adı Daha Önce Alınmış !")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request,messages.WARNING,"Bu E-mail Daha Önce Alınmış !")
                    return redirect("register")
                else:
                    user=User.objects.create_user(first_name=first_name,email=email,last_name=last_name,username=username,password=password)
                    user.save()
                    messages.add_message(request,messages.SUCCESS,"Hesabınız Oluşturuldu !")
                    return redirect("login")
            
        else:
            messages.add_message(request,messages.WARNING,"Parolalar Eşleşmiyor !")
            return redirect("register")
    else:
        return render(request,'user/register.html')



    
    
def logout(request):

    if request.method=="POST":
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,"Oturumunuz Kapatıldı !")
        return redirect("HomePage")
    



