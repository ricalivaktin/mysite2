from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
        
class Category(models.Model):
    name = models.CharField(max_length=155)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    
    def __str__(self):
        return f"{self.name}"
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blogs") 
    description = RichTextField(max_length=3500)
    is_active = models.BooleanField()
    is_home = models.BooleanField()
    slug = models.SlugField(null=True,blank=True,unique=True,db_index=True,editable= False)
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)#bire cok ilişki içindi bu 
    #! yabancı anahatr : ismi neden bu cunku başka  modelın anahtarı kullanılıyor burda categorilize etmek  için 
    #! on_delete=models.SET_NULL    alırsa oncesınde : null=True  olmali
    #! on_delete=models.CASCADE     alırsa o kategori silindigindeon abglı bloıglarda sılınır
    #! on_delete=models.SET_DEFAULT alırsa  öncesinde : default=1  (1 telefoın kategorısıne deng geliyordur) vs  olur
    #todo: coka cok ilişki turu 
    categories = models.ManyToManyField(Category,blank=True)
    
    def __str__(self):
        return f"{self.title}"
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
      



























#######################################
#######################################
#######################################

# class Blog(models.Model):
#     title = models.CharField(max_length=255)
#     #image = models.CharField(max_length=255)
#     image = models.ImageField(upload_to="blogs") 
#     # * kaydedılecek yerı belirlersin ya mevct dızınde ya başka bır dısınde 
#     # # NOTE 1 : açıklamasına bak aşagıda 
#     # description = models.TextField(max_length=3500)
#     description = RichTextField(max_length=3500)#! burda kullanıldı ckedıtor
#     is_active = models.BooleanField()
#     is_home = models.BooleanField()
#     #!
#     slug = models.SlugField(null=True,blank=True,unique=True,db_index=True,editable= False)
#     #?
#     def __str__(self):
#         return f"{self.title} "
    
#     def save(self,*args,**kwargs):
#         self.slug = slugify(self.title)
#         super().save(*args,**kwargs)
        
# #! burayı ıyı anlamak ıcın 159-ve 160 videoları izle   

  
    
    
# class Category(models.Model):
#     name = models.CharField(max_length=155)
#     #? NO! 1 :  ilkin magrations olussun ve var olana bu yenıler kaydedılsın dıye bunu  yapıyoruz: control ettık işlemler calısmıssa  bo ikiyi yapıyoruz
#     #! slug = models.SlugField(null=True,blank=True,unique=True,db_index=True,editable=False)
#     #? NO! 2 : null=FAlse  oluyor... 
#     slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)

    
    
    
#     def __str__(self):
#         return f"{self.name}"
    
#     def save(self,*args,**kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args,**kwargs)
    
#! burayı ıyı anlamak ıcın 159-ve 160 videoları izle  
   
   
##############
#ımage field için acıklama 
 # #NOTE :1 
    #image = models.CharField(max_length=255)
    # #! bu sadece isim saklar ve mevcut bır clasrden verı cekmen ıcın ısmı kullanmana baglı olur.. 
    # #! ama ya resım yuklemek ıstersen ? yada resim linkinden resmi almak istersen ?
    #todo:  o zaman ya = ImageField  veya  FileField kullanırsın Image sadece resım için file iste herhangi bir dosya alır farketmez ona 
    
    #NOTE :1 
    #APPMAİN İÇİDEKİ URLS.PY YE 
    # #! ımagefiels ve filefield için gerekli configrasyon ayarları
    #! from django.conf.urls.static import static # EKLENECEK 
    #! from django.conf import settings  # EKLENECEK 
    #! #urlpatterns  =[CONTENCTS CODE.. VAR BURDA ]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  # EKLENECEK 
    #TODO : DAHA ONCESINDE DE SENIN APPMAİN  İÇİNDEKİ SETTİNG.PY SUNLARI EKLMIS OLMAN LAZIM 
    #? MEDIA_ROOT = BASE_DIR / "uploads"
    #? MEDIA_URL = "/images/"   #! TAKMA İSİM VERECEZ BURDA  FİLE DOSYAMIZA ( gizlizlik )


    # bunlar tamamsa artık resım yonetım panelınden ulaşıla bılırdr 
############## 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#####################################
#####################################
#####################################
    
# class Blog(models.Model):
#     title = models.CharField(max_length=255)
#     image = models.CharField(max_length=255)
#     description = models.TextField(max_length=3500)
#     is_active = models.BooleanField()
#     is_home = models.BooleanField()
#     #! MODEL OLUŞTRULDUKTAN SONRA EKLENENLER BUNLAR
#     slug = models.SlugField(null=True,unique=True,db_index=True )

#     #! field alanlarına : null=True dersen     :  boş deger de kabul eder.. illa bır deger atamasanda olur demek olur 
#     #!                    default=False dersen :  varsayılanı false olur yanı  boş gecılemez illa bır sey girilmeli demek field alanı
#     #! CharField(bu alan default=False dir max_length = en fazla 255 girmelisin azi 1 dir )
#     def __str__(self):
#         # return f"{self.title} - {self.description} - {self.image} - {self.is_active} - {self.is_home}"
#         return f"{self.title} "
    
#     # def __str__(self):
#     #     def resim_control(resim):
#     #         resim = ""
#     #         if resim:
#     #             resim = "Ürün Resmi Var"
#     #         else:
#     #             resim = "Resim Yok"
#     #         return resim
#     #     def actif_mi_text(obj):
#     #         if obj:
#     #             return "Ürün activ mevcut"
#     #         else:
#     #             return "Ürün deactiv Mevcut Değil"
#     #     def homede_mi_text(obj):
#     #         if obj:
#     #             return "Ürün Ana Sayfada mevcut"
#     #         else:
#     #             return "Ürün  Ana Sayfada Mevcut Değil"
        
#     #     return f"{self.title} - {self.description} -{resim_control(self.image)} - {actif_mi_text(self.is_active)} - {homede_mi_text(self.is_home)} - "
    
# class Category(models.Model):
#     name = models.CharField(max_length=155)
    
#     def __str__(self):
#         return f"{self.name}"
    
    
    