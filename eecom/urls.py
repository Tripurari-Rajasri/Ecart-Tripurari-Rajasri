"""eecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as v
from admins import views as v1
from PIL import Image
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index,name='index'),
    path('digitalproducts/',v.digitalproducts,name='digitalproducts'),
    path('Furniture/',v.Furniture,name='Furniture'),
    path('clothing/',v.clothing,name='clothing'),
    path('Household/', v.Household, name='Household'),
    path('HOME/',v.HOME,name='HOME'),
    path('Register/',v.register,name='Register'),
    path('login/',v.login,name='login'),
    path('profile/',v.profile,name='profile'),
    path('uproducts/',v.uproducts,name='uproducts'),
    path('buy_product/<int:id>/buy/',v.buy_product,name='buy_product'),
    path('buy_product/',v.buy_product,name='buy_product'),
    path('purchase/',v.purchase,name='purchase'),
    path('apurchase/', v1.apurchase, name='apurchase'),
    path('ulogout/',v.ulogout,name='ulogout'),
    path('alogout/',v1.alogout,name='alogout'),
    path('contact/',v.contact,name='contact'),
    path('ahome/',v1.ahome,name='ahome'),
    path('last/',v.last,name='last'),






    path('alogin/',v1.alogin,name='alogin'),
    path('addproducts/', v1.addproducts, name='addproducts'),
    path('viewproducts/',v1.viewproducts,name='viewproducts'),
]


urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
