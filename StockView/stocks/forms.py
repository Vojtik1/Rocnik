from django import forms

class StockForm(forms.Form):
    symbol = forms.CharField(label='Stock Symbol', max_length=10)

    def clean_symbol(self):
        symbol = self.cleaned_data.get('symbol')
        return symbol.upper()
