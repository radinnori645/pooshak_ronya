from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from . models import Profile


class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(
        label="شماره تلفن:", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن خود را وارد کنید'}),
        required = False
    )
    address1 = forms.CharField(
        label="آدرس :", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس منزل خود را وارد کنید'}),
        required = False
    )
    address2 = forms.CharField(
        label="آدرس:", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس محل کار خود را وارد کنید (الزامی نیست)'}),
        required = False
    )
    city = forms.CharField(
        label="شهر:", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شهر خود را وارد کنید'}),
        required = False
    )
    state = forms.CharField(
        label="منطقه:", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'منطقه خود را وارد کنید'}),
        required = False
    )
    zipcode = forms.CharField(
        label="کد پستی:", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کد پستی خود را وارد کنید'}),
        required = False
    )
    country = forms.CharField(
        label="کشور", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کشور خود را وارد کنید'}),
        required = False
    )

    class Meta:
        model = Profile
        fields=('phone','address1','address2','city','state','zipcode', 'country')

class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="رمز:",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'رمز بالای هشت کاراکتر خود را وارد کنید'
            }
        )
    )
    new_password2 = forms.CharField(
        label="رمز:",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'رمز خود را دوباره وارد کنید'
            }
        )
    )
    class Meta:
        model = User
        fields = ['new_password1','new_password2']

class UpdateUserForm( UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="نام:", 
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'})
        ,required = False
    )
    last_name = forms.CharField(
        label="نام خانوادگی:", 
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی  خود را وارد کنید'})
        ,required = False
    )
    email = forms.EmailField(
        label="ایمیل:", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
       , required = False
    )
    username = forms.CharField(
        label="نام کاربری:", 
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری خود را وارد کنید'})
        ,required = False
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="نام:", 
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label="نام خانوادگی:", 
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی  خود را وارد کنید'})
    )
    email = forms.EmailField(
        label="ایمیل:", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
    )
    username = forms.CharField(
        label="نام کاربری:", 
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری خود را وارد کنید'})
    )
    password1 = forms.CharField(
        label="رمز:",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'رمز بالای هشت کاراکتر خود را وارد کنید'
            }
        )
    )
    password2 = forms.CharField(
        label="رمز:",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'رمز خود را دوباره وارد کنید'
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
