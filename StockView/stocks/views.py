# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock, Portfolio
from .forms import StockForm
import yfinance as yf
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import StockSearchForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import View
from django import forms

def stock_list(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            if fetch_and_save_stock_data(symbol):
                return redirect('stock_list')
            else:
                message = f"Stock ticker {symbol} does not exist."
                return render(request, 'stock/stock_list.html', {'form': form, 'message': message})

    else:
        form = StockForm()

    stocks = Stock.objects.all()
    return render(request, 'stock/stock_list.html', {'stocks': stocks, 'form': form})

def fetch_and_save_stock_data(symbol):
    stock = yf.Ticker(symbol)
    stock_info = stock.info

    if stock_info.get('shortName', 'N/A') != 'N/A':
        stock_instance, created = Stock.objects.get_or_create(symbol=symbol)
        stock_instance.company_name = stock_info.get('shortName', 'N/A')
        stock_instance.exchange = stock_info.get('exchange', 'N/A')
        stock_instance.sector = stock_info.get('sector', 'N/A')
        stock_instance.industry = stock_info.get('industry', 'N/A')
        stock_instance.current_price = stock_info.get('currentPrice', None)
        stock_instance.daily_change = stock_info.get('regularMarketChange', None)
        stock_instance.volume = stock_info.get('volume', None)
        stock_instance.week_52_high = stock_info.get('fiftyTwoWeekHigh', None)
        stock_instance.week_52_low = stock_info.get('fiftyTwoWeekLow', None)
        stock_instance.pe_ratio = stock_info.get('trailingPE', None)
        stock_instance.market_cap = stock_info.get('marketCap', None)
        stock_instance.dividend_yield = stock_info.get('dividendYield', None)
        stock_instance.beta = stock_info.get('beta', None)
        stock_instance.earnings_yield = stock_info.get('earningsYield', None)
        stock_instance.forward_pe_ratio = stock_info.get('forwardPE', None)
        stock_instance.price_sales_ratio = stock_info.get('priceToSalesTrailing12Months', None)
        stock_instance.price_book_ratio = stock_info.get('priceToBook', None)
        stock_instance.long_business_summary = stock_info.get('longBusinessSummary', 'N/A')
        stock_instance.save()

        return True
    else:
        return False

def fetch_stock(request, symbol):
    if fetch_and_save_stock_data(symbol):
        message = f"Data for stock {symbol} has been successfully fetched and saved."
    else:
        message = f"Stock ticker {symbol} does not exist."

    return render(request, 'stock/fetch_stock.html', {'symbol': symbol, 'message': message})

def edit_stock(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock.symbol = form.cleaned_data['symbol']
            if fetch_and_save_stock_data(stock.symbol):
                stock.save()
                return redirect('stock_list')
            else:
                message = f"Stock ticker {stock.symbol} does not exist."
                return render(request, 'stock/edit_stock.html', {'form': form, 'message': message, 'stock': stock})
    else:
        form = StockForm(initial={'symbol': stock.symbol})

    return render(request, 'stock/edit_stock.html', {'form': form, 'stock': stock})

def delete_stock(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    if request.method == 'POST':
        stock.delete()
        return redirect('stock_list')
    return render(request, 'stock/delete_stock.html', {'stock': stock})

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]


def stock_detail(request, symbol):
    stock = get_object_or_404(Stock, symbol=symbol)

    ticker = yf.Ticker(symbol)
    stock.current_price = ticker.history(period='1d')['Close'][0]
    try:
        stock.daily_change = ticker.info['regularMarketChange']
    except KeyError:
        stock.daily_change = None

    try:
        stock.volume = ticker.info['volume']
    except KeyError:
        stock.volume = None

    try:
        stock.fifty_two_week_high = ticker.info['fiftyTwoWeekHigh']
    except KeyError:
        stock.fifty_two_week_high = None

    try:
        stock.fifty_two_week_low = ticker.info['fiftyTwoWeekLow']
    except KeyError:
        stock.fifty_two_week_low = None

    try:
        stock.pe_ratio = ticker.info['trailingPE']
    except KeyError:
        stock.pe_ratio = None

    try:
        stock.market_cap = ticker.info['marketCap']
    except KeyError:
        stock.market_cap = None

    try:
        stock.dividend_yield = ticker.info['dividendYield'] * 100 if ticker.info['dividendYield'] else None
    except KeyError:
        stock.dividend_yield = None

    try:
        stock.beta = ticker.info['beta']
    except KeyError:
        stock.beta = None

    try:
        stock.earnings_yield = 1 / stock.pe_ratio if stock.pe_ratio else None
    except ZeroDivisionError:
        stock.earnings_yield = None

    try:
        stock.forward_pe_ratio = ticker.info['forwardPE']
    except KeyError:
        stock.forward_pe_ratio = None

    try:
        stock.price_to_sales_ratio = ticker.info['priceToSalesTrailing12Months']
    except KeyError:
        stock.price_to_sales_ratio = None

    try:
        stock.price_to_book_ratio = ticker.info['priceToBook']
    except KeyError:
        stock.price_to_book_ratio = None

    stock.long_business_summary = ticker.info['longBusinessSummary']

    stock.save()

    context = {
        'stock': stock,
        'current_price': stock.current_price,
        'daily_change': stock.daily_change,
        'volume': stock.volume,
        'week_52_high': stock.week_52_high,
        'week_52_low': stock.week_52_low,
        'pe_ratio': stock.pe_ratio,
        'market_cap': stock.market_cap,
        'dividend_yield': stock.dividend_yield,
        'beta': stock.beta,
        'earnings_yield': stock.earnings_yield,
        'forward_pe_ratio': stock.forward_pe_ratio,
        'price_sales_ratio': stock.price_sales_ratio,
        'price_book_ratio': stock.price_book_ratio,
        'long_business_summary': stock.long_business_summary,
    }
    return render(request, 'stock/stock_detail.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'stock/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def user_profile(request):
    # Zde můžete přidat kód pro získání informací o uživateli a vykreslení uživatelského profilu
    return render(request, 'stock/user_profile.html')

def index_view(request):
    return render(request, 'stock/index.html')

@login_required
def portfolio_view(request):
    # Získání portfolia aktuálně přihlášeného uživatele
    portfolio = Portfolio.objects.get(owner=request.user)
    return render(request, 'portfolio.html', {'portfolio': portfolio})


class AddToPortfolioForm(forms.Form):
    pass


class AddToPortfolioView(View):
    def post(self, request, stock_id):
        stock = Stock.objects.get(pk=stock_id)
        user = request.user
        portfolio, created = Portfolio.objects.get_or_create(owner=user)
        portfolio.stocks.add(stock)
        return redirect('stock_list')



