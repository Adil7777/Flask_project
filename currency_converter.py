from currency_converter import CurrencyConverter


def currency_converter(amount, from_currency, to_currency):
    c = CurrencyConverter()
    return c.convert(amount, from_currency, to_currency)
