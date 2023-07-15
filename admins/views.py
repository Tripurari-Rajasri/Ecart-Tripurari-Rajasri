from django.shortcuts import render
from .models import Products
from user.models import Register,Purchase
from PIL import Image


# Create your views here.
def alogin(request):
    if request.method == "POST":
        try:
            email = request.POST.get('cemail')
            paw = request.POST.get('paw')
            if email == 'admin@gmail.com' and paw == 'admin':
                return render(request, 'a_home.html')
            else:

                return render(request, 'a login.html')

        except Exception as e:
            print('Exception is e:', e)
            return render(request, 'a login.html')
    else:
        return render(request, 'a login.html')


def addproducts(request):
    if request.method == "POST":
        try:
            pname = request.POST.get('pname')
            pcat = request.POST.get('pcat')
            pcost = request.POST.get('pcost')
            pquality = request.POST.get('pquality')
            pdec = request.POST.get('pdec')
            pimage = request.FILES['pimage']
            data = Products(
                pname=pname,
                pcat=pcat,
                pcost=pcost,
                pquality=pquality,
                pdec=pdec,
                pimage=pimage
            )
            data.save()
            return render(request, 'addproducts.html')
        except Exception as e:
            print("Exception is:", e)
            return render(request, 'a_home.html')
    else:
        return render(request, 'addproducts.html')


def viewproducts(request):
    data = Products.objects.all()
    return render(request, 'viewproducts.html', {'products': data})

def apurchase(request):
    data=Purchase.objects.all()
    return render(request,'apurchase.html',{'data':data})


def alogout(request):
    return render(request,'index.html')


def ahome(request):
    return render(request,'a_home.html')