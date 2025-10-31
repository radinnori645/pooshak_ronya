from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm, UpdateUserInfo
from django.db.models import Q
import json
from cart.cart import Cart

from payment.forms import ShippingForm
from payment.models import ShippingAddress, Order, OrderItem


def order_details(request, pk):
    if request.user.is_authenticated:
        order = Order.objects.get(id=pk)
        items = OrderItem.objects.filter(order=pk)

        context= {
            'order':order,
            'items':items
        }
        return render(request, 'order_details.html', context)
    else:
        messages.success(request, 'دست رسی به این صفحه امکان پذیر نمی باشد')
        return redirect('home')


def user_orders(request):
    if request.user.is_authenticated:
        delivered_orders = Order.objects.filter(user=request.user, status='Delivered')
        other_orders = Order.objects.filter(user=request.user).exclude(status='Delivered')

        context = {
            'delivered': delivered_orders,
            'other': other_orders
        }
        return render(request, 'orders.html', context)
    else:
        messages.success(request, 'دست رسی به این صفحه امکان پذیر نمی باشد')
        return redirect('home')


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not searched:
            messages.success(request, 'چنین محصولی وجود ندارد')
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched': searched})
    return render(request, 'search.html', {})



def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shipping_user = ShippingAddress.objects.get(user__id = request.user.id)

        form = UpdateUserInfo(request.POST or None, instance = current_user)
        shipping_form = ShippingForm(request.POST or None, instance = shipping_user)

        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            
            messages.success(request, "اطلاعات کربری شما ویرایش شد")
            return redirect('home')
        return render(request, 'update_info.html', {'form':form, 'shipping_form':shipping_form})
    else:
        messages.success(request, "ابتدا باید ورود/ثبت نام کنید")
        return redirect('home')

def category_summary(request):
    all_cat = Category.objects.all()    
    return render(request, 'category_summary.html', {'category':all_cat})

def helloworld(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})

def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            curren_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = curren_user.old_cart

            if saved_cart:
                    converted_cart = json.loads(saved_cart)
                    cart = Cart(request)

                    for key, value in converted_cart.items():
                        cart.db_add(product=key, quantity=value)

            messages.success(request, "با موفقیت وارد شدید")
            return redirect("home")
        else:
            messages.success(request, "مشکلی در ورود وجود داشت")
            return redirect("login")
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("با موفقیت خارج شدید!"))
    return redirect("home")

def signup_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, ("اکانت شما با موفقیت ساخته شد"))
            return redirect("update_info")
        else:
            messages.success(request, ("مشکلی در ثبت نام شما پیش آمد"))
            return render(request, 'signup.html', {'form': form})
    else:  
        return render(request, 'signup.html', {'form': form})
    
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance = current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "پروفایل شما ویرایش شد")
            return redirect('home')
        return render(request, 'update_user.html', {'user_form':user_form})
    else:
        messages.success(request, "ابتدا باید ورود/ثبت نام کنید")
        return redirect('home')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == 'POST':
            form = UpdatePasswordForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'رمز با موفقیت ویرایش شد')
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')
        else:
            form = UpdatePasswordForm(current_user)
            return render (request, 'update_password.html', {'form': form})
    else:
        messages.success(request, 'اول باید ورود/ثبت نام کنید')
        return redirect('home')

def product(request,pk):
    products = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': products})

def category(request, cat):
    cat = cat.replace("-", " ")
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, "category": category})
    except Category.DoesNotExist:
        messages.success(request, "دسته‌بندی مورد نظر یافت نشد")
        return redirect("home")