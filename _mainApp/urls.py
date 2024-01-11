from django.urls import path
from . import views





urlpatterns = [
    path("",views.index_ihtihayc_hanem,name="home"),
    path("index/",views.index_ihtihayc_hanem,name="home"),
    path("blogs/",views.blogs_ihtiyac_hanem,name="blogs"),
    path("adding/",views.adding_ihtiyac_hanem,name="adding"),
    path("adding1/",views.adding1_ihtiyac_hanem,name="adding1"),
    path("category/<slug:slug>",views.category_ihtiyac_hanem,name="category_ihtiyac_hanem"),
    path("blogs/<slug:slug>",views.blogs_details_ihtiyac_hanem,name="blogs_details"),
]






















######################################
######################################
######################################


# urlpatterns = [
#     path("",views.index_ihtihayc_hanem,name="home"),
#     path("index/",views.index_ihtihayc_hanem,name="home"),
#     path("blogs/",views.blogs_ihtiyac_hanem,name="blogs"),
#     #* BURDA BLOG DETAYINI İD İLE ALIYORUZ İMDİ ARTIK SLUG İLE ALACAZ...URL ŞEMASINI DEGİŞTİRECEZ...
#     # path("blogs/<int:id>",views.blogs_details_ihtiyac_hanem,name="blogs_details")
#     #! catetgry için asagidakı
#     path("category/<slug:slug>",views.category_ihtiyac_hanem,name="category_ihtiyac_hanem"),
#     #! YENİ ŞEMA ŞEKLİ ...views.py içide güncellenecek bu fdogrultuda 
#     path("blogs/<slug:slug>",views.blogs_details_ihtiyac_hanem,name="blogs_details"),
# ]
