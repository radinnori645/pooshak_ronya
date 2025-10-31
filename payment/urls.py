from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('confim_order/', views.confim_order, name="confim_order"),
    path('process_order/', views.process_order, name="process_order"),
]

