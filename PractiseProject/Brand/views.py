from django.shortcuts import render,redirect
from . import forms
from . import models
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class AddBrandCreateView(CreateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'add_brand.html'
    success_url = reverse_lazy('add_brand')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)