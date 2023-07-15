from django.shortcuts import render,redirect
from .models import Register, Purchase
from admins.models import Products
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        try:
            cname = request.POST.get('cname')
            cemail = request.POST.get('cemail')
            paw = request.POST.get('paw')
            mno = request.POST.get('mno')
            addr = request.POST.get('addr')
            pincode = request.POST.get('pincode')
            data = Register(
                cname=cname,
                cemail=cemail,
                paw=paw,
                mno=mno,
                addr=addr,
                pincode=pincode,
            )
            data.save()
            return render(request, 'index.html')
        except Exception as e:
            print("Exception is:", e)
            return render(request, 'Register.html')
    else:
        return render(request, 'Register.html')


def login(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('cemail')
            paw = request.POST.get('paw')
            data = Register.objects.get(cemail=email, paw=paw)
            request.session['userid'] = data.cemail
            print(data)
            return render(request, 'HOME.html')
        except Exception as e:
            print("Exception is e:", e)
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def profile(request):
    try:
        uid = request.session['userid']
        print(uid)
        data = Register.objects.get(cemail=uid)
        return render(request, 'profile.html', {'profile': [data]})
    except Exception as e:
        print("Exception is:", e)
        return render(request, 'home.html')


def uproducts(request):
    data = Products.objects.all()
    return render(request, 'uproducts.html', {'Products': data})


def buy_product(request, id):
    if request.method == 'POST':
        uid = request.session['userid']
        cid = Register.objects.get(cemail=uid)
        products = Products.objects.get(id=id)
        data = Purchase(
            pname=products.pname,
            pcat=products.pcat,
            pcost=products.pcost,
            pquality=products.pquality,
            pdec=products.pdec,

            cid_id=cid.id,
            pid_id=id,
        )
        data.save()
        messages.success(request, 'product purchased successfully')
        return render(request, 'uproducts.html')
    else:
        messages.error(request, 'not purchased.')
        return redirect('uproducts')


def purchase(request):
        uid = request.session['userid']
        cdata = Register.objects.get(cemail=uid)
        cid = cdata.id
        data = Purchase.objects.filter(cid_id=cid)
        return render(request, 'purchase.html', {'data':data})


def ulogout(request):
    return render(request, 'index.html')

def contact(request):
    return render(request,'contact.html')


def digitalproducts(request):
    return render(request,'digitalproducts.html')


def Furniture(request):
    return render(request,'Furniture.html')


def clothing(request):
    return render(request,'clothing.html')


def Household(request):
    return render(request,'Household.html')


def HOME(request):
    return render(request,'HOME.html')


def last(request):
    return render(request,'last.html')