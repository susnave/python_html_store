from django.http import HttpResponse
from django.shortcuts import render
from .models import Product






def store(request):
    products= Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)


def cart(request):
   context = {}
   return render(request, 'store/cart.html', context)

   
def checkout(request):
 context = {}
 return render(request, 'store/checkout.html', context)


def resultado(request):
 busqueda=request.GET['busqueda']
 resultado=Product.objects.filter(name=busqueda)
 mensaje= "El resultado es: %s" %resultado[0]
 return HttpResponse (mensaje)




# Create your views here.


