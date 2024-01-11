from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.

def Entry(request,username,password):#! calısıyor ama  gırıs yapınce yonlendırmıyor...?
    #? yeni kullanıcı kayıt edıldı artık ıseteresn logın sayfasına aktar ısetersen aşagıdakı gıbı gırıs yap 
    #todo: kaydedılen ıle gırış...
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect("home")
    else:
        return render(request,"account/login.html",{"error":"UserName veya PassWord hatalidir !!!"})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]
        # Entry(request,username,password) #! calısıyor ama  gırıs yapınce yonlendırmıyor...?
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"account/login.html",{"error":"UserName veya PassWord hatalidir !!!"})
    
        
    return render(request,"account/login.html")





def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        
        username  = request.POST["username"]
        email     = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname  = request.POST["lastname"]
        password  = request.POST["password"]
        rpassword = request.POST["rpassword"]
        
        #list_user = [username,email,firstname,lastname,password,rpassword]
      
        
        if password == rpassword:
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html",{
                    "error":"Bu Username Kullanılıyor...!!!",
                    "username":username,
                    "email":email,
                    "firstname":firstname,
                    "lastname":lastname
                    })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"account/register.html",{
                        "error":"Bu E-mail Kullanılıyor...!!!",
                        "username":username,
                        "email":email,
                        "firstname":firstname,
                        "lastname":lastname,
                    })
                else:
                    #! buraya kadar gelmişşe kulanıcı oluşturula bılır deke bubılgıler ıle 
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    return redirect("login")
                    # Entry(request,username,password)    #! direk giriş istersen bu functionun ıcerıgını buraya ekle 
        else:
            return render(request,"account/register.html",{
                "error":"Parola Eşleşmiyor...!!!",
                "username":username,
                "email":email,
                "firstname":firstname,
                "lastname":lastname})

    return render(request,"account/register.html")
 
        
        
         
    
        
   


def logout_view(request):
    logout(request)
    return redirect("home")