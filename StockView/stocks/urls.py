# urls.py
from django.urls import path
from .views import stock_list, fetch_stock, edit_stock, delete_stock, stock_detail

urlpatterns = [
    path('', stock_list, name='stock_list'),
    path('fetch_stock/<str:symbol>/', fetch_stock, name='fetch_stock'),
    path('edit_stock/<int:stock_id>/', edit_stock, name='edit_stock'),
    path('delete_stock/<int:stock_id>/', delete_stock, name='delete_stock'),
    path('stock_detail/<str:symbol>/', stock_detail, name='stock_detail'),  # Nově přidaná cesta
]
