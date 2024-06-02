import yfinance as yf

def fetch_and_print_stock_data(symbol):
    stock = yf.Ticker(symbol)
    stock_info = stock.info
    print(stock_info)

# Zavolejte funkci s konkrétním symbolem akcie
fetch_and_print_stock_data("CRWD")
