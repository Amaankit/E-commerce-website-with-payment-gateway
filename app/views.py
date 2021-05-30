from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponseRedirect
from .models import Product,Cart,OrderPlaced,UserProfile
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.utils.decorators import method_decorator
#Home view
class HomeProductListView(ListView):
    model = Product
    template_name = "app/home.html"
    context_object_name='bottomWears'
    def get_queryset(self):
        return Product.objects.filter(category__in=['BWMENS','BWWOMENS'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topWears"] = Product.objects.filter(category__in=['TWMENS','TWWOMENS'])
        context["mobiles"] = Product.objects.filter(category='M')
        context["laptops"] = Product.objects.filter(category='L')
        # for pro in context["topWears"] :
            # print(pro.category,'edfdf')
            # print('--------------------------------------')
    
        return context
#Home View ends here


#Product detail view
class ProductDetailView(DetailView):
    model = Product
    template_name = "app/productdetail.html"
    context_object_name='product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            pid=self.kwargs['pk']
            # print("user is",self.request.user)
            # print('________________________________')
            context["product_in_cart"] = Cart.objects.filter(Q(user=self.request.user) & Q(product=pid)).exists()
        return context
#Product details view ends here

#Buynow View
@login_required
def buyNow(request,pk):
    user=request.user
    prod=Product.objects.get(id=pk)
    Cart(user=request.user, product=prod).save()
    return redirect(reverse_lazy('checkout'))
#Buynow View

#Views related to displaying products on home page
##################################################################################################
#Mobile View
class MobileListView(ListView):
    model = Product
    template_name = "app/mobile.html"
    context_object_name='mobiles'
    def get_queryset(self):
        data=self.kwargs['data']
        if data == 'all':
            return Product.objects.filter(category='M')
        elif data == 'samsung':
            return Product.objects.filter(category='M').filter(brand='Samsung')
        elif data == 'redmi':
            return Product.objects.filter(category='M').filter(brand='Redmi')
        elif data == 'below':
            return Product.objects.filter(category='M').filter(discounted_price__lt=10000)
        elif data == 'above':
            return Product.objects.filter(category='M').filter(discounted_price__gt=10000)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data=self.kwargs['data']

        if data == 'all':
            context["active"] = 'all'
        elif data == 'samsung':
            context["active"] = 'samsung'
        elif data == 'redmi':
            context["active"] = 'redmi'
        elif data == 'below':
            context["active"] = 'below'
        elif data == 'above':
            context["active"] = 'above'

        return context
#Mobile View ends here

#laptop view
class LaptopListView(ListView):
    model = Product
    template_name = "app/laptop.html"
    context_object_name='laptops'
    def get_queryset(self):
        data=self.kwargs['data']
        if data == 'all':
            return Product.objects.filter(category='L')
        elif data == 'dell':
            return Product.objects.filter(category='L').filter(brand='Dell')
        elif data == 'hp':
            return Product.objects.filter(category='L').filter(brand='HP')
        elif data == 'below':
            return Product.objects.filter(category='L').filter(discounted_price__lt=40000)
        elif data == 'above':
            return Product.objects.filter(category='L').filter(discounted_price__gt=40000)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data=self.kwargs['data']

        if data == 'all':
            context["active"] = 'all'
        elif data == 'dell':
            context["active"] = 'dell'
        elif data == 'hp':
            context["active"] = 'hp'
        elif data == 'below':
            context["active"] = 'below'
        elif data == 'above':
            context["active"] = 'above'

        return context
#laptop view

#Topwear View
class TopWearListView(ListView):
    model = Product
    template_name = "app/topwear.html"
    context_object_name='topwears'
    def get_queryset(self):
        data=self.kwargs['data']
        if data == 'all':
            return Product.objects.filter(category__in=['TWMENS','TWWOMENS'])
        elif data == 'mens':
            return Product.objects.filter(category='TWMENS')
        elif data == 'womens':
            return Product.objects.filter(category='TWWOMENS')    
        elif data == 'below':
            return Product.objects.filter(category__in=['TWMENS','TWWOMENS']).filter(discounted_price__lt=1000)
        elif data == 'above':
            return Product.objects.filter(category__in=['TWMENS','TWWOMENS']).filter(discounted_price__gt=1000)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data=self.kwargs['data']

        if data == 'all':
            context["active"] = 'all'
        elif data == 'mens':
            context["active"] = 'mens'
        elif data == 'womens':
            context["active"] = 'womens'
        elif data == 'below':
            context["active"] = 'below'
        elif data == 'above':
            context["active"] = 'above'

        return context
#Topwear View
#Bottomwear View
class BottomWearListView(ListView):
    model = Product
    template_name = "app/bottomwear.html"
    context_object_name='bottomwears'
    def get_queryset(self):
        data=self.kwargs['data']
        if data == 'all':
            return Product.objects.filter(category__in=['BWMENS','BWWOMENS'])
        elif data == 'mens':
            return Product.objects.filter(category='BWMENS')
        elif data == 'womens':
            return Product.objects.filter(category='BWWOMENS')    
        elif data == 'below':
            return Product.objects.filter(category__in=['BWMENS','BWWOMENS']).filter(discounted_price__lt=1000)
        elif data == 'above':
            return Product.objects.filter(category__in=['BWMENS','BWWOMENS']).filter(discounted_price__gt=1000)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data=self.kwargs['data']

        if data == 'all':
            context["active"] = 'all'
        elif data == 'mens':
            context["active"] = 'mens'
        elif data == 'womens':
            context["active"] = 'womens'
        elif data == 'below':
            context["active"] = 'below'
        elif data == 'above':
            context["active"] = 'above'

        return context
#Bottomwear View
#Views related to displaying products on home page ends here.
####################################################################################

#Payment View -This projects integrated with Paypal payment gateway.
@login_required
def payment(request):
    user=request.user
    cart_obj=Cart.objects.filter(user=user)

    cust_id= request.POST['custid']
    # print(cust_id)
    # print("||||||||||||||||||||||||||||||||||||---------") 

    customer=UserProfile.objects.get(id=cust_id)
    # print(customer)
    # print("||||||||||||||||||||||||||||||||||||") 
    # print(cust_id)
    for c in cart_obj:

        productins=Product.objects.get(id=c.product.id)
        OrderPlaced(user=user,userprofile=customer,product=productins, quantity=c.quantity ).save()
        c.delete()
    return redirect(reverse_lazy('orders'))


#OrderPlaced View
@method_decorator(login_required, name='dispatch')
class OrderPlacedListView(ListView):
    model = OrderPlaced
    template_name = "app/orders.html"
    context_object_name='placed_order'
    def get_queryset(self):
        return OrderPlaced.objects.filter(user=self.request.user)
##OrderPlaced View ends here  

#Customer RegistrationView
class CustomerRegistrationView(View):
    def get(self,request):
        fm=UserRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':fm})
    def post(self,request):
       # print("ddddddddddddddddddddddddddddddd")
        fm=UserRegistrationForm(request.POST)
        print(fm)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Congratulations!! You're registered successfully.")
            return HttpResponseRedirect(reverse_lazy('login'))
        return render(request, 'app/customerregistration.html', {'form':fm})
#Customer RegistrationView ends here

#User Profile View            
@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    def get(self,request):
        fm=UserProfileForm()
        return render(request, 'app/profile.html', {'form':fm,'active':'active'})
    def post(self,request):
       # print("ddddddddddddddddddddddddddddddd")
        fm=UserProfileForm(request.POST)
        if fm.is_valid():
            user=request.user
            # print(user)
            name=fm.cleaned_data['name']
            landmark=fm.cleaned_data['landmark']
            locality=fm.cleaned_data['locality']
            city=fm.cleaned_data['city']
            zipcode=fm.cleaned_data['zipcode']
            state=fm.cleaned_data['state']
            obj=UserProfile(user=user, name=name,landmark=landmark,city=city,zipcode=zipcode,state=state, locality=locality)
            obj.save()
            messages.success(request,"Congratulations!! You're registered successfully.")
        return render(request, 'app/profile.html', {'form':fm,'active':'active'})
#User Profile View ends here

#Address Show view
@method_decorator(login_required, name='dispatch')
class AddressListView(ListView):
    model = UserProfile
    template_name = "app/address.html"
    context_object_name="address"
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = 'active'
        return context
#Address Show view ends here

#Add to cart View
@login_required    
def addToCart(request):
    product_id=request.GET.get('product_id')
    # print(product_id)
    prod=Product.objects.get(id=product_id)
    # print(prod)
    try:
        cartprod=Cart.objects.get(Q(user=request.user) & Q(product=prod))
            
    except:
        cartprod=None
    if not cartprod:
        Cart(user=request.user, product=prod).save()
    return redirect(reverse_lazy('show_cart'))
    

#Add to cart View ends here

#show cart View
class ShowCartView(LoginRequiredMixin,View):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('show_cart')
    def get(self,request):
        # print('123242424242425')
        user= request.user
        # print(user)
        cart= Cart.objects.filter(user=user)
        # print("------------------------------------------------------------")
        # print(cart)
        cart_prod=[p for p in Cart.objects.all() if p.user==user]
        amount=0.0
        totalAmount=0.0
        shippingCharges=50.0
        if cart_prod:
            for cp in cart_prod:
                tempAmount=(cp.product.discounted_price * cp.quantity)
                amount+=tempAmount
            totalAmount=amount+shippingCharges
            return render(request,'app/addtocart.html',{'cart':cart,'totalAmount':totalAmount,'amount':amount})
        else:
            return render(request,'app/emptycart.html')
#show cart View ends here      

#ALter Cart View Called by AJAX  
def alterCart(request,operator):
    # print()
    # print("||||||||||||||||||")
    # print(request.get_full_path)
    if request.method == "GET":
        pid=request.GET.get("pid")
        # print(pid)
        prod=Product.objects.get(id=pid)
        c=Cart.objects.get(Q(product=pid) & Q(user=request.user))
        # print(c)
        if operator=='pl':
            c.quantity+=1
            c.save()
        elif operator=='mn':
            c.quantity-=1
            c.save()
        else:
            c.delete()
        
        # print("------------------------------")
        cart_prod=[p for p in Cart.objects.all() if p.user==request.user]
        amount=0.0
        totalAmount=0.0
        shippingCharges=50.0
        for cp in cart_prod:
                tempAmount=(cp.product.discounted_price * cp.quantity)
                amount+=tempAmount
        totalAmount=amount+shippingCharges
        # print('amount',amount,"total",totalAmount)
        data={
            "amount":amount,
            "totalAmount":totalAmount,
            "quantity":c.quantity
        }
        return JsonResponse(data)
#ALter Cart View ends here


#Check Out View
@login_required
def checkout(request):
    user = request.user
    cart_obj = Cart.objects.filter(user=user)
    address = UserProfile.objects.filter(user=user)
    # print(address)
    cart_prod=[p for p in Cart.objects.all() if p.user==request.user]
    amount=0.0
    totalAmount=0.0
    shippingCharges=50.0
    if cart_prod:
        for cp in cart_prod:
            tempAmount=(cp.product.discounted_price * cp.quantity)
            amount+=tempAmount
        totalAmount=amount+shippingCharges
    return render(request, 'app/checkout.html',{'cart_obj':cart_obj,'address':address,'totalAmount':totalAmount})
#Check Out View ends here

#Display Cart called by ajax
def displayCart(request):
    if request.method == "GET":
        cartobj=Cart.objects.filter(user=request.user)
        lencartobj=cartobj.count()
        data={
            "lencartobj":lencartobj
            
        }
        return JsonResponse(data)