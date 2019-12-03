from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('addstock.html', views.addstock, name="addstock"),
    path('delete/<stock_id>', views.delete, name="delete"),
    path('delete_stock.html', views.delete_stock, name="delete_stock"),
]

