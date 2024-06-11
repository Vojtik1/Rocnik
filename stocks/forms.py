from django import forms

class StockForm(forms.Form):
    symbol = forms.CharField(label='Stock Symbol', max_length=10)

    def clean_symbol(self):
        symbol = self.cleaned_data.get('symbol')
        return symbol.upper()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class StockSearchForm(forms.Form):
     query = forms.CharField(label='Vyhledat akcii', max_length=100)