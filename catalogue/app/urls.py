from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('detailproduk', views.detailproduk, name='detailproduk'),
]