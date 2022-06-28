import requests
from bs4 import BeautifulSoup
import time

# create a function to get price of cryptocurrency


def get_latest_crypto_price(coin):
    url = f'https://www.google.com/search?q={coin}price'
    # make a request to the website
    HTML = requests.get(url)
    # Parsse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')
    return (
        soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
        .find({'div': 'BNeawe iBp4i AP7Wnd'})
        .text
    )


price = get_latest_crypto_price('bitcoin')
print(f'BITCOIN price : {price}')
