from forex_python.converter import CurrencyRates
c = CurrencyRates()
c.get_rates('USD')
c.get_rate('USD', 'THB')
