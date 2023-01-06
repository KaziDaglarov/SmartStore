from django.shortcuts import render
from .models import Phone
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


class PhonesView(ListView):
    model = Phone
    queryset = Phone.objects.filter(draft=False)
    context_object_name = 'phones'
    template_name = 'store/phone_list.html'




class PhoneDetailView(DetailView):
    slug_field = 'url'
    model = Phone




