# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock
from .forms import StockForm
import yfinance as yf

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
        stock_instance.current_price = stock_info.get('regularMarketPrice', 'N/A')
        stock_instance.daily_change = stock_info.get('regularMarketChange', 'N/A')
        stock_instance.volume = stock_info.get('regularMarketVolume', 'N/A')
        stock_instance.high_price_52 = stock_info.get('fiftyTwoWeekHigh', 'N/A')
        stock_instance.low_price_52 = stock_info.get('fiftyTwoWeekLow', 'N/A')
        stock_instance.pe_ratio = stock_info.get('forwardPE', 'N/A')
        stock_instance.market_cap = stock_info.get('marketCap', 'N/A')
        stock_instance.dividend_yield = stock_info.get('dividendYield', 'N/A')
        stock_instance.beta = stock_info.get('beta', 'N/A')
        stock_instance.earnings_yield = stock_info.get('earningsYield', 'N/A')
        stock_instance.forward_pe = stock_info.get('forwardPE', 'N/A')
        stock_instance.price_sales_ratio = stock_info.get('priceToSalesTrailing12Months', 'N/A')
        stock_instance.price_book_ratio = stock_info.get('priceToBook', 'N/A')


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

def stock_detail(request, symbol):
    stock = Stock.objects.get(symbol=symbol)
    return render(request, 'stock/stock_detail.html', {'stock': stock})





