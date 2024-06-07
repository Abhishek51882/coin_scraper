import requests
from bs4 import BeautifulSoup

class CoinMarketCapScraper:
    BASE_URL = 'https://coinmarketcap.com/currencies/'

    def scrape(self, coin):
        url = f'{self.BASE_URL}{coin}/'
        response = requests.get(url)
        if response.status_code != 200:
            return {'error': 'Coin not found'}
        
        soup = BeautifulSoup(response.text, 'html.parser')
        data = self.parse_data(soup)
        return data

def parse_data(self, soup):
    # Find the elements containing the required information
    price_element = soup.find('div', {'class': 'priceValue'})
    market_cap_element = soup.find('div', {'class': 'marketCapValue'})
    volume_element = soup.find('div', {'class': 'volumeValue'})
    circulating_supply_element = soup.find('div', {'class': 'circulatingSupplyValue'})
    total_supply_element = soup.find('div', {'class': 'totalSupplyValue'})
    diluted_market_cap_element = soup.find('div', {'class': 'dilutedMarketCapValue'})
    
    # Extract text from the found elements
    price = price_element.text if price_element else None
    market_cap = market_cap_element.text if market_cap_element else None
    volume = volume_element.text if volume_element else None
    circulating_supply = circulating_supply_element.text if circulating_supply_element else None
    total_supply = total_supply_element.text if total_supply_element else None
    diluted_market_cap = diluted_market_cap_element.text if diluted_market_cap_element else None
    
    # Construct the dictionary with the scraped data
    data = {
        'price': price,
        'market_cap': market_cap,
        'volume': volume,
        'circulating_supply': circulating_supply,
        'total_supply': total_supply,
        'diluted_market_cap': diluted_market_cap
    }
    
    return data

