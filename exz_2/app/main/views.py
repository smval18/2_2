from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .models import *
from .forms import *


class IndexList(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'app/index.html'

    def get_queryset(self):
        return Product.objects.all()[:5]


def profile(request):
    order = Order.objects.filter(user=request.user)

    context = {
        "orders": order,
    }

    return render(request, 'app/profile.html', context)


class ServiceList(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'app/services.html'

    def get_queryset(self):
        return Product.objects.all()


def service_detail(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.product_id = id
            instance.save()
    else:
        form = OrderForm(initial={'user': request.user.pk, 'product': id})

    return render(request, "app/service_detail.html", {'product': product, 'form': form})


class RegisterView(generic.CreateView):
    model = AdvUser
    form_class = RegisterForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')

