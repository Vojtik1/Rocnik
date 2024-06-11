from django.contrib.auth.models import User
from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=100)
    exchange = models.CharField(max_length=50)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    current_price = models.FloatField(null=True)
    daily_change = models.FloatField(null=True)
    volume = models.IntegerField(null=True)
    week_52_high = models.FloatField(null=True)
    week_52_low = models.FloatField(null=True)
    pe_ratio = models.FloatField(null=True)
    market_cap = models.BigIntegerField(null=True)
    dividend_yield = models.FloatField(null=True)
    beta = models.FloatField(null=True)
    earnings_yield = models.FloatField(null=True)
    forward_pe_ratio = models.FloatField(null=True)
    price_sales_ratio = models.FloatField(null=True)
    price_book_ratio = models.FloatField(null=True)
    long_business_summary = models.TextField(null=True)


    def save(self, *args, **kwargs):
        self.symbol = self.symbol.upper()
        super(Stock, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
        ordering = ['symbol']

    def __str__(self):
        return self.symbol

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='portfolios', on_delete=models.CASCADE)
    stocks = models.ManyToManyField(Stock, related_name='portfolios', through='PortfolioStock')

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
        ordering = ['name']

    def __str__(self):
        return self.name

class PortfolioStock(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)  # Počet akcií v portfoliu
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Cena nákupu
    purchase_date = models.DateField(null=True, blank=True)  # Datum nákupu

    class Meta:
        verbose_name = "Portfolio Stock"
        verbose_name_plural = "Portfolio Stocks"
        ordering = ['portfolio']

    def __str__(self):
        return f"{self.portfolio.name} - {self.stock.symbol}"


