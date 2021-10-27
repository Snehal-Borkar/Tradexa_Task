from django.shortcuts import render

# Create your views here.
from .models import Product

def show_product(request):
    products=Product.objects.using('products_db').all()
    return render(request,"users/products.html",{"products":products})




def product_details(request,id):
    item=Product.objects.using('products_db').get(id=id)
    return render(request,"users/item_detail.html",{"item":item})
