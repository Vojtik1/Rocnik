from django.contrib import admin
from .models import User, Stock, Portfolio, PortfolioStock

admin.site.register(User)
admin.site.register(Stock)
admin.site.register(Portfolio)
admin.site.register(PortfolioStock)
