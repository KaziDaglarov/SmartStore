from django.urls import path
from .views import *



urlpatterns = [
    path('', PhonesView.as_view()),
    path('<slug:slug>/', PhoneDetailView.as_view(), name='phone'),

]