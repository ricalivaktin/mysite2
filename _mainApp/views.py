from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from _mainApp.models import Blog ,Category

#!  ### Create your views here. ###


########################################
def index_ihtihayc_hanem(request):
  
    
    context = {
        "categories":Category.objects.all(),
        "_blogs_": Blog.objects.all(), 
        "blogs": Blog.objects.filter(is_home=True,is_active=True), 
        }
    return render(request,"_mainApp/index.html",context)


def blogs_ihtiyac_hanem(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {
        "categories":Category.objects.all(),
        "_blogs_": Blog.objects.all(), 
        "blogs": Blog.objects.filter(is_active=True), 
        
        }
    return render(request,"_mainApp/blogs.html",context)




#bu prod ekler
def adding_ihtiyac_hanem(request):
    if not request.user.is_authenticated:
        return redirect("register")
    ######
    prod_infos = []
    if request.method == "POST":
        
        title=request.POST["title"]
        image=request.POST["image"]
        description=request.POST["description"]
        is_active=request.POST["is_active"]
        is_home=request.POST["is_home"]
        categories=request.POST["categories"]
        
        list_prod = [title,image,description,is_active,is_home,categories]
        for i in list_prod:
            prod_infos.append(i)
            
        prod_infos.append("ÜRÜN BAŞARI İLE EKLENDİ")
        #####
        #! creating prod process
        Blog.objects.create(title=str(title),image=f"blogs/{str(image)}",description=str(description),is_active=is_active,is_home=is_home)
        #todo : burda ürün eklenır...
        
    else:
        prod_infos.append("Bu Liste Boş - Ürün oluşmadi !!! ")
    ######  
    context = {
        "categories":Category.objects.all(),  
        "prod_infos":prod_infos
    }
    ######
    return render(request,"_mainApp/adding.html",context)
#bu ctagory ekler
def adding1_ihtiyac_hanem(request):
    if not request.user.is_authenticated:
        return redirect("register")
    ######
    prod_infos = []
    if request.method == "POST":
        
        name=request.POST["name"]
        prod_infos.append(name)
        prod_infos.append("Category BAŞARI İLE EKLENDİ")
        #####
        #! creating prod process
        Category.objects.create(name=str(name))
        #todo : burda ürün eklenır...
        
    else:
        prod_infos.append("Bu Liste Boş - Category oluşmadi !!! ")
    ######  
    context = {
        "categories":Category.objects.all(),  
        "prod_infos":prod_infos
    }
    ######
    return render(request,"_mainApp/adding1.html",context)






def blogs_details_ihtiyac_hanem(request,slug):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {
        "categories":Category.objects.all(),
        "blog" : Blog.objects.get(slug=slug),
    }
    return render(request,"_mainApp/blogs-details.html",context)


def category_ihtiyac_hanem(request,slug):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {
        "categories":Category.objects.all(),
        "_blogs_": Blog.objects.all(), 
        # "blogs": Blog.objects.filter(is_active=True,category__slug=slug ), 
        # "blogs": Category.objects.get(slug=slug).blog_set.all(),
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "selected_category":slug
        
        }
    return render(request,"_mainApp/blogs.html",context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
####################################
####################################
####################################

#todo veri tabenından :   kayıt listesınden sonra 
#* BURDA BLOG DETAYINI İD İLE ALIYORUZ İMDİ ARTIK SLUG İLE ALACAZ...
#! İD
# def blogs_details_ihtiyac_hanem(request,id):
#     context = {
#         "categories":Category.objects.all(),
#         "_blogs_": Blog.objects.all(), 
#         "blogs": Blog.objects.filter(is_active=True), 
#         "blog" : Blog.objects.get(pk=id) ,
#     }
#     blog = Blog.objects.get(pk=id)
#     return render(request,"_mainApp/blogs-details.html",context)

#! SLUG
# def blogs_details_ihtiyac_hanem(request,slug):
#     context = {
#         "categories":Category.objects.all(),
#         "blog" : Blog.objects.get(slug=slug),
#     }
#     return render(request,"_mainApp/blogs-details.html",context)
























###############################
###############################
###############################
###############################


###############################

#todo : http://127.0.0.1:8000/ 

# data = {
    
#     "index":["index.html"],
#     "blogs":[
#         {"id":1,"title":"Medine Misvak'i","image":"prod1.jpg","is_active":True,"is_home":False,"description":"Güzel bir ürün"},
#         {"id":2,"title":"Mekke Misvak'i","image":"prod2.jpg","is_active":True,"is_home":False,"description":"harika bir ürün"},
#         {"id":3,"title":"Kuddus Misvak'i","image":"prod3.jpg","is_active":True,"is_home":True,"description":"Enfes bir ürün"},
#         {"id":4,"title":"Kahire Misvak'i","image":"prod4.jpg","is_active":True,"is_home":True,"description":"idare bir ürün"},
#         {"id":5,"title":"istanbul Misvak'i","image":"prod5.jpg","is_active":True,"is_home":True,"description":"hoş bir ürün"},
#         {"id":6,"title":"Poma Misvak'i","image":"new_prod.jpg","is_active":True,"is_home":False,"description":"siyah bir ürün"},   
#     ],
#     "blogs/1":["blogs-details.html"],
# }

########################################
########################################
########################################

#! bu yapay data obj gore idi 
# def index_ihtihayc_hanem(request):
#     # return HttpResponse("ihtiyac_hanem base page-1...")
#     context = {
#         "categories":list(data_.keys()),
#         "blogs":data["blogs"],
#         }
#     return render(request,"_mainApp/index.html",context)

#todo veri tabenından :   kayıt listesınden sonra 
# def index_ihtihayc_hanem(request):
#     context = {
#         "categories":Category.objects.all(),
#         "_blogs_": Blog.objects.all(), 
#         "blogs": Blog.objects.filter(is_home=True,is_active=True), 
#         }
#     return render(request,"_mainApp/index.html",context)


#! bu yapay data obj gore idi 
# def blogs_ihtiyac_hanem(request):
#     # return HttpResponse("ihtiyac_hanem blogs page-2...")
#     context = {
#         "categories":list(data.keys()),
#         "blogs":data["blogs"],    
#     }
#     return render(request,"_mainApp/blogs.html",context)

#todo veri tabenından :  kayıt listesınden sonra 
# def blogs_ihtiyac_hanem(request):
#     context = {
#         "categories":Category.objects.all(),
#         "_blogs_": Blog.objects.all(), 
#         "blogs": Blog.objects.filter(is_active=True), 
        
#         }
#     return render(request,"_mainApp/blogs.html",context)



#! bu yapay data obj gore idi 
# def blogs_details_ihtiyac_hanem(request,id):
#     # return HttpResponse(f"ihtiyac_hanem blogs details page-3...|| details page = {id}")
    
#     #! 1 şekil uzun yol 
#     # blogs = data["blogs"]
#     # selectedBlog = None
#     # for blog in blogs:
#     #     if blog["id"] == id:
#     #         selectedBlog = blog
#     #! 2 şekil kısa yol  campration usulu 
#     blogs = data["blogs"]
#     selectedBlog =  [blog for blog in blogs if blog["id"] == id][0]#! sondakı [0] ekı 
#     # !onun lıstenın cıkan sonucun ılkını demek 
    

#     return render(request,"_mainApp/blogs-details.html",{
#         "DB":id,
#         "categories":list(data.keys()),
#         "blog":selectedBlog 
#         }
#     )

#todo veri tabenından :   kayıt listesınden sonra 
# def blogs_details_ihtiyac_hanem(request,id):
#     context = {
#         "categories":Category.objects.all(),
#         "_blogs_": Blog.objects.all(), 
#         "blogs": Blog.objects.filter(is_active=True), 
#         "blog" : Blog.objects.get(pk=id) ,
#     }
#     blog = Blog.objects.get(pk=id)
#     return render(request,"_mainApp/blogs-details.html",context)
