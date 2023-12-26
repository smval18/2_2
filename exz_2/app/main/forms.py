from django import forms
from .models import Product, AdvUser, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "desc", "photo")


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AdvUser
        fields = ("username", "password", "photo")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {'user': forms.HiddenInput, 'product': forms.HiddenInput}
