import requests # ! Allows API requests in Python

def get_price(symbol):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': symbol
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'd6587b9f-1cab-4713-aae9-465f3c90537a'
    }

    response = requests.get(url, params=parameters, headers=headers)
    return response.json().get('data').get(symbol).get('quote').get('USD').get('price')


# def euro_conversion(amount):
    url = 'https://api.apilayer.com/exchangerates_data/convert?'
    parameters = {
        'amount': amount,
        'from': 'USD',
        'to': 'EUR'
    }
    headers = {
        'apikey': env('SECRET_EURO_KEY')
    }

    response = requests.get(url, params=parameters, headers=headers)
    return response.json().get('result')

def get_trade(symbol): # ! Converts to Euro from USD
    trade = get_price(symbol)
    return trade