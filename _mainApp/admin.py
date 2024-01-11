from django.contrib import admin
from .models import Blog,Category
#html yorumlaması ıcın 
from django.utils.safestring import mark_safe

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug","selected_categories",)
    list_editable = ("is_active","is_home",) 
    search_fields = ("title","image","description",)  
    readonly_fields = ("slug",)
    #bloglardakı categorı lere gore sıralama fıltreleme
    # list_filter = ("category","is_active","is_home",)
    list_filter = ("is_active","is_home","categories",)
    
    def selected_categories(self,obj):
        html = "<select name='action' required=''><option value='' selected=''>---------</option>"
        for category in obj.categories.all():
            html +=  f"<option value='{category.name}'>{category.name}</option>"
        html += "</select>"
        return mark_safe(html)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug",)
    readonly_fields = ("slug",)






admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)














#####################################
#####################################
#####################################



#todo: özelleştirilmiş sinif blog
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ("title","is_active","is_home","slug",)# panel üzeründe başlıkları gosterırı 
#     list_editable = ("is_active","is_home",) #! panel üzerinden ozele gitmeden  guncelleme sağlar 
#     search_fields = ("title","image","description",)  #! arama yapılacak alanlar yazdık bunun ıcın panalde bır arama kutusu cıkar search box 
#     # readonly_fields = ("description",) # ! bu alanı sadece okuna bılır yapar  edıt ve guncelleme kabul etmez
#     readonly_fields = ("slug",)
    
# #! buraya ekledıgımız admın uygulama panel tarafıoında gozukur
# # admin.site.register(Blog)
# # admin.site.register(Category)

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name","slug",)
#     readonly_fields = ("slug",)

# #todo : özelleştirilmiş hali ile panelde başlıklar cıkar 
# admin.site.register(Blog,BlogAdmin)#todo : özelleştirmek istersen ( class ile yukarıya ekle )
# admin.site.register(Category,CategoryAdmin)