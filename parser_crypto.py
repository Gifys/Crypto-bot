from bs4 import BeautifulSoup
import requests

def course(name_crypto):
    url = f'https://coinmarketcap.com/currencies/{name_crypto}/'

    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    teme = soup.find(class_="priceValue").string

    return teme

# Not used
def shops_url(name_crypto):
    return f'https://coinmarketcap.com/ru/currencies/{name_crypto}/markets/'



def news(name_crypto):
    url = f'https://coinmarketcap.com/ru/currencies/{name_crypto}/news/'

    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    teme = soup.find(class_="sc-1eb5slv-0 svowul-3 ddtKCV")

    return teme



