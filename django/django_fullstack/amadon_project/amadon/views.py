from django.shortcuts import render, redirect
from .models import Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "amadon/index.html", context)

def buy(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])
        
        product = Product.objects.get(id=product_id)
        total_charge = product.price * quantity
        
        request.session['last_order_charge'] = float(total_charge)
        
        if 'total_quantity' not in request.session:
            request.session['total_quantity'] = 0
        if 'total_amount' not in request.session:
            request.session['total_amount'] = 0
            
        request.session['total_quantity'] += quantity
        request.session['total_amount'] += float(total_charge)
        
        return redirect('/amadon/checkout')
    return redirect('/amadon/')

def checkout(request):
    return render(request, "amadon/checkout.html")
