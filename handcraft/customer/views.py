from typing import Any, Dict
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView
from store.models import craft
from .models import cart,Orders
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models.query import QuerySet
from django.db.models import Sum
from .forms import UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.decorators import method_decorator




# decorators

def signinrequerd(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"sign in requerd")
            return redirect('signinu')
    return inner



# Create your views here.

# @method_decorator(signinrequerd,name='dispatch')
class customerhomeview(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['data']=craft.objects.all()
        return context
    



@method_decorator(signinrequerd,name='dispatch')
class addcart(View):
    def get(self,request,*args,**kwargs):
        prod=craft.objects.get(id=kwargs.get('pid'))
        user=request.user
        cart.objects.create(craft=prod,user=user)
        messages.success(request,'product added to cart successfully')
        return redirect('home')
        
@method_decorator(signinrequerd,name='dispatch')
class cartshowview(ListView):
    template_name='cartshow.html'
    model=cart
    context_object_name='cartitem'


    def get_queryset(self):
        Cart=cart.objects.filter(user=self.request.user,status='cart')
    
        return {"item":Cart}
    
    
def cartdeleteview(request,id):

    cd=cart.objects.get(id=id)
    cd.delete()
    return redirect('cartshow')


@method_decorator(signinrequerd,name='dispatch')
class checkoutview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"checkout.html")
    def post(self,request,*args,**kwargs):
        id=kwargs.get('cid')
        Cart=cart.objects.get(id=id)
        Craft=Cart.craft
        user=request.user
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        Orders.objects.create(craft=Craft,user=user,address=address,phone=phone)
        cart.status="order placed"
        Cart.save()
        messages.success(request,"order placed successfully!!!")
        return redirect('home')
    
    
@method_decorator(signinrequerd,name='dispatch')
class ordershow(ListView):
    template_name='orders.html'
    model=Orders
    context_object_name='orderditems'

    def get_queryset(self):
        orders=Orders.objects.filter(user=self.request.user)
        return {'order':orders}



def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        password_form = PasswordChangeForm(user, request.POST)
        if form.is_valid() and password_form.is_valid():
            form.save()
            password_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('home')
    else:
        form = UserProfileForm(instance=user)
        password_form = PasswordChangeForm(user=request.user)

    return render(request, 'userprofile.html', {'form': form, 'password_form': password_form})