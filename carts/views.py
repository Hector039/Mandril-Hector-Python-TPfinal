from django.shortcuts import render
from users.models import CustomUser
from products.models import Product
from products.forms import ProductSearchForm
from .models import Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def getUserCart(req, uid):
    try:
        cart = Cart.objects.filter(userId=uid)
        for prod in cart:
            prod.subtotal = prod.productId.price * prod.quantity

        total = 0
        for subTotal in cart:
            total = total + subTotal.subtotal
        
        return render(req, "cart-detail.html", {"avatar_url": req.session["avatar_path"], "last_login": req.session["last_login"], "cart": cart, "total": total})
    except Exception as error:
        messages.error(req, error)
        return render(req, "cart-detail.html", {"avatar_url": req.session["avatar_path"], "last_login": req.session["last_login"], "cart": cart, "total": total})
    
    

@login_required
def getCart(req, uid):
    return getUserCart(req, uid)

@login_required
def emptyCart(req, uid):
    try:
        cart = Cart.objects.filter(userId=uid).delete()
        if cart[0] != 0:
            messages.success(req, 'Your cart is now empty.')
            return getUserCart(req, uid)
    except Exception as error:
        messages.error(req, error)
        return getUserCart(req, uid)

@login_required
def deleteProductCart(req, uid, pid):
    try:
        user = CustomUser.objects.get(id=uid)
        product = Product.objects.get(id=pid)
        cart = Cart.objects.get(userId=user, productId=product).delete()
        if cart[0] != 0:
            messages.success(req, f'{product.title} was successfully removed.')
            return getUserCart(req, uid)
    except Exception as error:
        messages.error(req, error)
        return getUserCart(req, uid)

@login_required
def buyCart(req, uid):
    return getUserCart(req, uid, msg='Coming soon.')

@login_required
def addToCart(req, uid, pid):
    searchForm = ProductSearchForm(req.GET)
    if req.method == 'POST':
        try:
            user = CustomUser.objects.get(pk=uid)
            product = Product.objects.get(pk=pid)
            newProductToCart = Cart(id=None, userId=user, productId=product, quantity=req.POST["quantity"])
            newProductToCart.save()
            products = Product.objects.all()
            messages.success(req, f"{product.title} was added to your cart")
            return render(req, "home.html", {"avatar_url": req.session["avatar_path"], "last_login": req.session["last_login"], "products": products, 'searchForm': searchForm})
        except Exception as error:
            products = Product.objects.all()
            messages.error(req, error)
            return render(req, "home.html", {"avatar_url": req.session["avatar_path"], "last_login": req.session["last_login"], "products": products, 'searchForm': searchForm})
        
    return getUserCart(req, uid)
