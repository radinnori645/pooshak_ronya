from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):    
    shipping_full_name = forms.CharField(
    label="نام و نام خوانوادگی ", 
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام و نام خانوادگی  خود را وارد کنید'}),
    required = True,

    )
    shipping_email = forms.CharField(
    label="ایمیل ", 
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ایمیل خود را وارد کنید'}),
    required = False, 

    )
    shipping_address1 = forms.CharField(
    label="آدرس :", 
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرسن منزل خود را وارد کنید'}),
    required = True,

    )
    shipping_address2 = forms.CharField(
    label="آدرس:", 
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس محل کار خود را وارد کنید (الزامی نیست)'}),
    required = False,

    )
    shipping_city = forms.CharField(
    label="شهر:", 
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شهر خود را وارد کنید'}),
    required = True,

    )
    shipping_state = forms.CharField(
    label="منطقه:", 
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'منطقه خود را وارد کنید'}),
    required = False,

    )
    shipping_zipcode = forms.CharField(
    label="کد پستی:", 
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کد پستی خود را وارد کنید'}),
    required = False,

    )
    shipping_country = forms.CharField(
    label="کشور", 
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کشور خود را وارد کنید'}),
    required = True,

    )

    class Meta:
        model = ShippingAddress
        fields=[
            'shipping_full_name',
            'shipping_email',
            'shipping_address1',
            'shipping_address2',
            'shipping_city',
            'shipping_state',
            'shipping_zipcode',
            'shipping_country',
        ]

        exclude = ['user',]