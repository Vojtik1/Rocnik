# urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import stock_list, fetch_stock, edit_stock, delete_stock, stock_detail, index_view, portfolio_view, AddToPortfolioView
from . import views

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('stock_list', stock_list, name='stock_list'),
    path('add_to_portfolio/<int:stock_id>/', AddToPortfolioView.as_view(), name='add_to_portfolio'),
    path('fetch_stock/<str:symbol>/', fetch_stock, name='fetch_stock'),
    path('edit_stock/<int:stock_id>/', edit_stock, name='edit_stock'),
    path('delete_stock/<int:stock_id>/', delete_stock, name='delete_stock'),
    path('stock_detail/<str:symbol>/', stock_detail, name='stock_detail'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('accounts/profile/', views.user_profile, name='user_profile'),
    path('portfolio/', portfolio_view, name='portfolio'),
]
